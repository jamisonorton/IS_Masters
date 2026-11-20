<?php
require_once dirname(__DIR__) . '/repositories/userPDO.php';
require_once dirname(__DIR__) . '/repositories/studentPDO.php';

function validateUserProfile($name, $email)
{
    $name = trim((string)$name); $email = strtolower(trim((string)$email));
    if ($name === '' || mb_strlen($name) > 120) throw new InvalidArgumentException('Enter a name using 1 to 120 characters.');
    if (mb_strlen($email) > 254 || !filter_var($email, FILTER_VALIDATE_EMAIL)) throw new InvalidArgumentException('Enter a valid email address.');
    return [$name, $email];
}

function validateNewPassword($password)
{
    if (!is_string($password) || strlen($password) < 12 || strlen($password) > 72) {
        throw new InvalidArgumentException('Use a password between 12 and 72 bytes.');
    }
}

function registerUser($pdo, $input)
{
    [$name, $email] = validateUserProfile($input['full_name'] ?? '', $input['email'] ?? '');
    $password = (string)($input['password'] ?? '');
    $confirmation = (string)($input['confirm_password'] ?? '');
    $role = (string)($input['role'] ?? '');
    validateNewPassword($password);
    if (!hash_equals($password, $confirmation)) throw new InvalidArgumentException('Passwords do not match.');
    if (!in_array($role, ['Student', 'Tutor'], true)) throw new InvalidArgumentException('Choose Student or Tutor.');

    $pdo->beginTransaction();
    try {
        $id = createUserRecord($pdo, $name, $email, password_hash($password, PASSWORD_DEFAULT), $role);
        if ($role === 'Student') linkStudentToUser($pdo, $name, $email, $id);
        $pdo->commit();
        return $id;
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        if ($e instanceof PDOException && strpos(strtolower($e->getMessage()), 'unique') !== false) {
            throw new InvalidArgumentException('An account with that email already exists.');
        }
        throw $e;
    }
}

function authenticateUser($pdo, $email, $password)
{
    $user = findUserByEmail($pdo, $email);
    if (!$user || $user['status'] !== 'Active' || !password_verify((string)$password, $user['password_hash'])) return false;
    if (password_needs_rehash($user['password_hash'], PASSWORD_DEFAULT)) {
        updateUserPasswordRecord($pdo, $user['user_id'], password_hash((string)$password, PASSWORD_DEFAULT));
    }
    return findUserById($pdo, $user['user_id']);
}

function updateOwnProfile($pdo, $userId, $name, $email)
{
    [$name, $email] = validateUserProfile($name, $email);
    $pdo->beginTransaction();
    try {
        updateUserProfileRecord($pdo, $userId, $name, $email);
        $pdo->commit();
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        if ($e instanceof PDOException && strpos(strtolower($e->getMessage()), 'unique') !== false) {
            throw new InvalidArgumentException('That email address is already in use.');
        }
        throw $e;
    }
}

function changeOwnPassword($pdo, $user, $current, $new, $confirmation)
{
    if (!password_verify((string)$current, $user['password_hash'])) throw new InvalidArgumentException('Current password is incorrect.');
    validateNewPassword((string)$new);
    if (!hash_equals((string)$new, (string)$confirmation)) throw new InvalidArgumentException('New passwords do not match.');
    updateUserPasswordRecord($pdo, $user['user_id'], password_hash((string)$new, PASSWORD_DEFAULT));
}

function changeUserRole($pdo, $targetId, $role)
{
    if (!in_array($role, ['Student', 'Tutor', 'Administrator'], true)) throw new InvalidArgumentException('Choose a valid role.');
    $pdo->beginTransaction();
    try {
        $target = findUserById($pdo, $targetId);
        if (!$target) throw new RuntimeException('Account not found.');
        if ($target['role'] === 'Administrator' && $target['status'] === 'Active' && $role !== 'Administrator'
            && countOtherActiveAdministrators($pdo, $targetId) === 0) {
            throw new DomainException('The last active administrator cannot be changed to another role.');
        }
        if ($role === 'Student' && !findStudentByUserId($pdo, $targetId)) {
            linkStudentToUser($pdo, $target['full_name'], $target['email'], $targetId);
        }
        updateUserRoleRecord($pdo, $targetId, $role);
        $pdo->commit();
    } catch (Throwable $e) { if ($pdo->inTransaction()) $pdo->rollBack(); throw $e; }
}

function changeUserStatus($pdo, $targetId, $status)
{
    if (!in_array($status, ['Active', 'Inactive'], true)) throw new InvalidArgumentException('Choose a valid status.');
    $pdo->beginTransaction();
    try {
        $target = findUserById($pdo, $targetId);
        if (!$target) throw new RuntimeException('Account not found.');
        if ($target['role'] === 'Administrator' && $target['status'] === 'Active' && $status === 'Inactive'
            && countOtherActiveAdministrators($pdo, $targetId) === 0) {
            throw new DomainException('The last active administrator cannot be deactivated.');
        }
        updateUserStatusRecord($pdo, $targetId, $status);
        $pdo->commit();
    } catch (Throwable $e) { if ($pdo->inTransaction()) $pdo->rollBack(); throw $e; }
}

function removeUserIfAllowed($pdo, $targetId)
{
    $pdo->beginTransaction();
    try {
        $target = findUserById($pdo, $targetId);
        if (!$target) throw new RuntimeException('Account not found.');
        if ($target['role'] === 'Administrator' && $target['status'] === 'Active' && countOtherActiveAdministrators($pdo, $targetId) === 0) {
            throw new DomainException('The last active administrator cannot be deleted.');
        }
        if (userTutoringRequestCount($pdo, $targetId) > 0) {
            throw new DomainException('This account has tutoring requests. Those records are retained, so the account cannot be deleted.');
        }
        $stmt = $pdo->prepare('DELETE FROM students WHERE user_id = ?');
        $stmt->execute([(int)$targetId]);
        deleteUserRecord($pdo, $targetId);
        $pdo->commit();
    } catch (Throwable $e) {
        if ($pdo->inTransaction()) $pdo->rollBack();
        throw $e;
    }
}

<?php
function findUserByEmail($pdo, $email)
{
    $stmt = $pdo->prepare('SELECT * FROM users WHERE email = ? COLLATE NOCASE');
    $stmt->execute([trim($email)]);
    return $stmt->fetch();
}

function findUserById($pdo, $userId)
{
    $stmt = $pdo->prepare('SELECT user_id, full_name, email, password_hash, role, status, created_at FROM users WHERE user_id = ?');
    $stmt->execute([(int)$userId]);
    return $stmt->fetch();
}

function createUserRecord($pdo, $name, $email, $hash, $role)
{
    $stmt = $pdo->prepare("INSERT INTO users(full_name,email,password_hash,role,status) VALUES(?,?,?,?, 'Active')");
    $stmt->execute([$name, strtolower(trim($email)), $hash, $role]);
    return (int)$pdo->lastInsertId();
}

function updateUserProfileRecord($pdo, $userId, $name, $email)
{
    $stmt = $pdo->prepare('UPDATE users SET full_name = ?, email = ? WHERE user_id = ?');
    $stmt->execute([$name, strtolower(trim($email)), (int)$userId]);
    $student = $pdo->prepare('UPDATE students SET student_name = ?, student_email = ? WHERE user_id = ?');
    $student->execute([$name, strtolower(trim($email)), (int)$userId]);
}

function updateUserPasswordRecord($pdo, $userId, $hash)
{
    $stmt = $pdo->prepare('UPDATE users SET password_hash = ? WHERE user_id = ?');
    $stmt->execute([$hash, (int)$userId]);
}

function searchUsers($pdo, $search, $role, $status)
{
    $sql = 'SELECT user_id, full_name, email, role, status, created_at FROM users WHERE 1 = 1';
    $args = [];
    if ($search !== '') {
        $sql .= ' AND (full_name LIKE ? OR email LIKE ?)';
        $term = '%' . str_replace(['%', '_'], ['\\%', '\\_'], $search) . '%';
        $args[] = $term; $args[] = $term;
    }
    if ($role !== '') { $sql .= ' AND role = ?'; $args[] = $role; }
    if ($status !== '') { $sql .= ' AND status = ?'; $args[] = $status; }
    $sql .= ' ORDER BY full_name COLLATE NOCASE, user_id';
    $stmt = $pdo->prepare($sql); $stmt->execute($args); return $stmt->fetchAll();
}

function updateUserRoleRecord($pdo, $userId, $role)
{
    $stmt = $pdo->prepare('UPDATE users SET role = ? WHERE user_id = ?');
    $stmt->execute([$role, (int)$userId]);
    return $stmt->rowCount() === 1;
}

function updateUserStatusRecord($pdo, $userId, $status)
{
    $stmt = $pdo->prepare('UPDATE users SET status = ? WHERE user_id = ?');
    $stmt->execute([$status, (int)$userId]);
    return $stmt->rowCount() === 1;
}

function countOtherActiveAdministrators($pdo, $exceptUserId)
{
    $stmt = $pdo->prepare("SELECT COUNT(*) FROM users WHERE role = 'Administrator' AND status = 'Active' AND user_id <> ?");
    $stmt->execute([(int)$exceptUserId]);
    return (int)$stmt->fetchColumn();
}

function userTutoringRequestCount($pdo, $userId)
{
    $stmt = $pdo->prepare('SELECT COUNT(*) FROM tutoring_requests r JOIN students s ON s.student_id = r.student_id WHERE s.user_id = ?');
    $stmt->execute([(int)$userId]);
    return (int)$stmt->fetchColumn();
}

function deleteUserRecord($pdo, $userId)
{
    $stmt = $pdo->prepare('DELETE FROM users WHERE user_id = ?');
    $stmt->execute([(int)$userId]);
    return $stmt->rowCount() === 1;
}

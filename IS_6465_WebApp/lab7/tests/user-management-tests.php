<?php
require_once dirname(__DIR__) . '/config/db.php';
require_once dirname(__DIR__) . '/services/userService.php';
$pdo = new PDO('sqlite::memory:');
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
$pdo->exec('PRAGMA foreign_keys = ON');
$pdo->exec(file_get_contents(dirname(__DIR__) . '/database/setup-database.sql'));
migrateUserManagementSchema($pdo);
$passed = 0; $failed = 0;
function checkUserTest($condition, $label)
{
    global $passed, $failed;
    if ($condition) { $passed++; echo "PASS: {$label}" . PHP_EOL; }
    else { $failed++; echo "FAIL: {$label}" . PHP_EOL; }
}
function expectUserTestException($callable, $class, $label)
{
    try { $callable(); checkUserTest(false, $label); }
    catch (Throwable $e) { checkUserTest($e instanceof $class, $label); }
}

$studentInput = ['full_name'=>'Jordan Lee','email'=>'jordan@example.edu','password'=>'StudyHub!Pass2026','confirm_password'=>'StudyHub!Pass2026','role'=>'Student'];
$studentId = registerUser($pdo, $studentInput);
$student = findUserById($pdo, $studentId);
checkUserTest($student && $student['status'] === 'Active' && $student['role'] === 'Student', 'UM-01 Student account is Active');
checkUserTest($student && $student['password_hash'] !== $studentInput['password'] && password_verify($studentInput['password'], $student['password_hash']), 'UM-01 only a verified password hash is stored');
checkUserTest((int)$pdo->query('SELECT user_id FROM students WHERE student_email="jordan@example.edu"')->fetchColumn() === $studentId, 'UM-01 student account links to the existing STUDENTS entity');
expectUserTestException(function () use ($pdo, $studentInput) { registerUser($pdo, $studentInput); }, InvalidArgumentException::class, 'UM-01 duplicate email is rejected');
$tutorInput = ['full_name'=>'Taylor Tutor','email'=>'taylor@example.edu','password'=>'TutorPass!2026','confirm_password'=>'TutorPass!2026','role'=>'Tutor'];
$tutorId = registerUser($pdo, $tutorInput);
checkUserTest(findUserById($pdo, $tutorId)['role'] === 'Tutor', 'UM-01 Tutor account is supported');
$adminId = createUserRecord($pdo, 'Morgan Admin', 'admin@example.edu', password_hash('AdminPass!2026', PASSWORD_DEFAULT), 'Administrator');
expectUserTestException(function () use ($pdo, $studentId) { changeUserRole($pdo, $studentId, 'Superuser'); }, InvalidArgumentException::class, 'UM-06 invalid role value is rejected');
checkUserTest(authenticateUser($pdo, 'jordan@example.edu', 'StudyHub!Pass2026')['user_id'] === $studentId, 'UM-09 valid credentials authenticate');
checkUserTest(authenticateUser($pdo, 'jordan@example.edu', 'wrong-password') === false, 'UM-09 invalid password is rejected');
changeUserRole($pdo, $tutorId, 'Student');
checkUserTest(findStudentByUserId($pdo, $tutorId) !== false, 'UM-06 role change to Student provisions a linked student record');
changeUserStatus($pdo, $studentId, 'Inactive');
checkUserTest(authenticateUser($pdo, 'jordan@example.edu', 'StudyHub!Pass2026') === false, 'UM-07 and UM-09 inactive account cannot authenticate');
changeUserStatus($pdo, $studentId, 'Active');
updateOwnProfile($pdo, $studentId, 'Jordan Lee Updated', 'jordan.updated@example.edu');
checkUserTest(findUserById($pdo, $studentId)['full_name'] === 'Jordan Lee Updated', 'UM-04 profile fields can be updated');
$current = findUserById($pdo, $studentId);
changeOwnPassword($pdo, $current, 'StudyHub!Pass2026', 'A-new-Study-Password-2026', 'A-new-Study-Password-2026');
checkUserTest(authenticateUser($pdo, 'jordan.updated@example.edu', 'A-new-Study-Password-2026') !== false, 'UM-05 new password works');
checkUserTest(authenticateUser($pdo, 'jordan.updated@example.edu', 'StudyHub!Pass2026') === false, 'UM-05 old password no longer works');
$studentRecord = findStudentByUserId($pdo, $studentId);
$request = $pdo->prepare("INSERT INTO tutoring_requests(student_id,course,topic,preferred_date,preferred_time) VALUES(?, 'IS 6465', 'Lab retention test', '2026-12-01', 'Morning')");
$request->execute([(int)$studentRecord['student_id']]);
expectUserTestException(function () use ($pdo, $studentId) { removeUserIfAllowed($pdo, $studentId); }, DomainException::class, 'UM-08 account with related tutoring requests cannot be deleted');
checkUserTest((int)$pdo->query('SELECT COUNT(*) FROM tutoring_requests WHERE topic="Lab retention test"')->fetchColumn() === 1, 'UM-08 blocked deletion retains the tutoring request');
expectUserTestException(function () use ($pdo, $adminId) { changeUserStatus($pdo, $adminId, 'Inactive'); }, DomainException::class, 'UM-07 last active administrator is protected');
$admin = findUserById($pdo, $adminId);
expectUserTestException(function () use ($pdo, $adminId) { removeUserIfAllowed($pdo, $adminId); }, DomainException::class, 'UM-08 last active administrator cannot be deleted');
$rows = searchUsers($pdo, 'Jordan', '', 'Active');
checkUserTest(count($rows) === 1 && (int)$rows[0]['user_id'] === $studentId, 'UM-03 admin search filters name and status');
checkUserTest((int)$pdo->query('SELECT COUNT(*) FROM users')->fetchColumn() === 3, 'Rejected changes do not add accounts');
echo "Results: {$passed} passed, {$failed} failed" . PHP_EOL;
exit($failed > 0 ? 1 : 0);

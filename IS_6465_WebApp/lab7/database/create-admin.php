<?php
// Run from the command line only: php database/create-admin.php
if (PHP_SAPI !== 'cli') {
    http_response_code(404);
    exit('Not found');
}

require_once __DIR__ . '/../config/db.php';
require_once __DIR__ . '/../repositories/userPDO.php';
require_once __DIR__ . '/../services/userService.php';

$pdo = openDatabase();
$activeAdmins = (int)$pdo->query(
    "SELECT COUNT(*) FROM users WHERE role = 'Administrator' AND status = 'Active'"
)->fetchColumn();
if ($activeAdmins > 0) {
    fwrite(STDERR, "An active administrator already exists.\n");
    exit(1);
}

$arguments = array_slice($argv, 1);
if (count($arguments) === 3) {
    [$name, $email, $password] = $arguments;
} elseif (count($arguments) === 0) {
    $name = trim((string)readline('Administrator full name: '));
    $email = trim((string)readline('Administrator email: '));
    $isTerminal = function_exists('posix_isatty') && posix_isatty(STDIN);
    if ($isTerminal) system('stty -echo');
    fwrite(STDOUT, 'Password (12 to 72 bytes): ');
    $password = rtrim((string)fgets(STDIN), "\r\n");
    if ($isTerminal) {
        system('stty echo');
        fwrite(STDOUT, PHP_EOL);
    }
} else {
    fwrite(STDERR, "Usage: php create-admin.php [\"Full Name\" email password]\n");
    exit(2);
}

try {
    [$name, $email] = validateUserProfile($name, $email);
    validateNewPassword($password);
    $userId = createUserRecord(
        $pdo,
        $name,
        $email,
        password_hash($password, PASSWORD_DEFAULT),
        'Administrator'
    );
    fwrite(STDOUT, "Administrator account created with user ID {$userId}.\n");
} catch (Throwable $e) {
    fwrite(STDERR, $e->getMessage() . "\n");
    exit(1);
}

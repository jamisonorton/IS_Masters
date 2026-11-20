<?php
if (PHP_SAPI !== 'cli') { http_response_code(404); exit('Not found'); }
require_once dirname(__DIR__, 2) . '/config/db.php';
require_once dirname(__DIR__, 2) . '/repositories/userPDO.php';
require_once dirname(__DIR__, 2) . '/services/userService.php';
$pdo = openDatabase();
$exists = (int)$pdo->query("SELECT COUNT(*) FROM users WHERE role='Administrator' AND status='Active'")->fetchColumn();
if ($exists > 0) { fwrite(STDERR, "An active administrator already exists.\n"); exit(1); }
$name = trim((string)readline('Administrator full name: '));
$email = trim((string)readline('Administrator email: '));
$isTerminal = function_exists('posix_isatty') && posix_isatty(STDIN);
if ($isTerminal) system('stty -echo');
fwrite(STDOUT, 'Password (12 to 72 bytes): ');
$password = rtrim((string)fgets(STDIN), "\r\n");
if ($isTerminal) { system('stty echo'); fwrite(STDOUT, PHP_EOL); }
try {
    [$name, $email] = validateUserProfile($name, $email);
    validateNewPassword($password);
    $id = createUserRecord($pdo, $name, $email, password_hash($password, PASSWORD_DEFAULT), 'Administrator');
    fwrite(STDOUT, "Administrator account created with user ID {$id}.\n");
} catch (Throwable $e) {
    fwrite(STDERR, $e->getMessage() . "\n"); exit(1);
}

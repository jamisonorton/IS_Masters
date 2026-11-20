<?php
require_once dirname(__DIR__) . '/repositories/userPDO.php';
require_once __DIR__ . '/urls.php';

function startSecureSession()
{
    if (session_status() === PHP_SESSION_ACTIVE) return;
    $https = !empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off';
    session_set_cookie_params([
        'lifetime' => 0,
        'path' => '/',
        'secure' => $https,
        'httponly' => true,
        'samesite' => 'Lax'
    ]);
    ini_set('session.use_strict_mode', '1');
    session_start();
}

function csrfToken()
{
    startSecureSession();
    if (empty($_SESSION['csrf_token'])) $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
    return $_SESSION['csrf_token'];
}

function verifyCsrfToken($input)
{
    startSecureSession();
    $sent = is_array($input) ? (string)($input['csrf_token'] ?? '') : '';
    if (empty($_SESSION['csrf_token']) || !hash_equals($_SESSION['csrf_token'], $sent)) {
        http_response_code(403);
        exit('The form expired or could not be verified. Please go back and try again.');
    }
}

function requireLogin($pdo)
{
    startSecureSession();
    if (empty($_SESSION['user_id'])) {
        header('Location: ' . appUrl('php/login.php'), true, 303); exit;
    }
    if (time() - (int)($_SESSION['last_activity'] ?? 0) > 1200) {
        logoutSession(); header('Location: ' . appUrl('php/login.php?expired=1'), true, 303); exit;
    }
    $user = findUserById($pdo, (int)$_SESSION['user_id']);
    if (!$user || $user['status'] !== 'Active') {
        logoutSession(); header('Location: ' . appUrl('php/login.php?inactive=1'), true, 303); exit;
    }
    $_SESSION['last_activity'] = time();
    $_SESSION['display_name'] = $user['full_name'];
    $_SESSION['role'] = $user['role'];
    return $user;
}

function requireRole($user, $allowedRoles)
{
    if (!in_array($user['role'], $allowedRoles, true)) {
        http_response_code(403); exit('You are not authorized to perform this action.');
    }
}

function logoutSession()
{
    startSecureSession();
    $_SESSION = [];
    if (ini_get('session.use_cookies')) {
        $params = session_get_cookie_params();
        setcookie(session_name(), '', [
            'expires' => time() - 42000,
            'path' => $params['path'],
            'domain' => $params['domain'],
            'secure' => $params['secure'],
            'httponly' => $params['httponly'],
            'samesite' => $params['samesite'] ?? 'Lax'
        ]);
    }
    session_destroy();
}

function currentUserId()
{
    startSecureSession();
    return (int)($_SESSION['user_id'] ?? 0);
}

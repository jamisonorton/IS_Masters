<?php
require_once __DIR__ . '/../config/db.php';
require_once __DIR__ . '/../services/userService.php';
require_once __DIR__ . '/../includes/auth.php';
startSecureSession();
$error = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    verifyCsrfToken($_POST);
    $user = authenticateUser(openDatabase(), $_POST['email'] ?? '', $_POST['password'] ?? '');
    if (!$user) $error = 'Invalid email or password.';
    else {
        session_regenerate_id(true);
        $_SESSION['user_id'] = (int)$user['user_id'];
        $_SESSION['display_name'] = $user['full_name'];
        $_SESSION['role'] = $user['role'];
        $_SESSION['last_activity'] = time();
        unset($_SESSION['registration_success']);
        $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
        header('Location: profile.php', true, 303); exit;
    }
} elseif ($_SERVER['REQUEST_METHOD'] !== 'GET') { http_response_code(405); exit('Method not allowed'); }
$notice = $_SESSION['registration_success'] ?? '';
unset($_SESSION['registration_success']);
require __DIR__ . '/../includes/header.php'; require __DIR__ . '/../includes/nav.php'; ?>
<main class="container py-4 form-container"><h1>Log in</h1>
<?php if ($notice): ?><div class="alert alert-success"><?= htmlspecialchars($notice, ENT_QUOTES, 'UTF-8') ?></div><?php endif; ?>
<?php if (!empty($_GET['logged_out'])): ?><div class="alert alert-info">You have been logged out.</div><?php endif; ?>
<?php if (!empty($_GET['expired']) || !empty($_GET['inactive'])): ?><div class="alert alert-warning">Your session ended. Log in again to continue.</div><?php endif; ?>
<?php if ($error): ?><div class="alert alert-danger"><?= htmlspecialchars($error, ENT_QUOTES, 'UTF-8') ?></div><?php endif; ?>
<form method="post" class="vstack gap-3">
<input type="hidden" name="csrf_token" value="<?= htmlspecialchars(csrfToken(), ENT_QUOTES, 'UTF-8') ?>">
<div><label class="form-label" for="email">Email</label><input class="form-control" id="email" name="email" type="email" required autocomplete="username" value="<?= htmlspecialchars((string)($_POST['email'] ?? ''), ENT_QUOTES, 'UTF-8') ?>"></div>
<div><label class="form-label" for="password">Password</label><input class="form-control" id="password" name="password" type="password" required autocomplete="current-password"></div>
<button class="btn btn-primary">Log In</button></form><p class="mt-3"><a href="register.php">Create an account</a></p></main><?php require __DIR__ . '/../includes/footer.php'; ?>

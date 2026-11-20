<?php
require_once __DIR__ . '/../config/db.php'; require_once __DIR__ . '/../services/userService.php'; require_once __DIR__ . '/../includes/auth.php';
$pdo = openDatabase(); $user = requireLogin($pdo); $error = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    verifyCsrfToken($_POST);
    try {
        changeOwnPassword($pdo, $user, $_POST['current_password'] ?? '', $_POST['new_password'] ?? '', $_POST['confirm_password'] ?? '');
        session_regenerate_id(true); $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
        header('Location: profile.php?password_changed=1', true, 303); exit;
    } catch (InvalidArgumentException $e) { $error = $e->getMessage(); }
    catch (Throwable $e) { error_log($e->getMessage()); $error = 'Unable to change password.'; }
} elseif ($_SERVER['REQUEST_METHOD'] !== 'GET') { http_response_code(405); exit('Method not allowed'); }
require __DIR__ . '/../includes/header.php'; require __DIR__ . '/../includes/nav.php'; ?>
<main class="container py-4 form-container"><h1>Change Password</h1>
<?php if ($error): ?><div class="alert alert-danger"><?= htmlspecialchars($error, ENT_QUOTES, 'UTF-8') ?></div><?php endif; ?>
<form method="post" class="vstack gap-3"><input type="hidden" name="csrf_token" value="<?= htmlspecialchars(csrfToken(), ENT_QUOTES, 'UTF-8') ?>">
<div><label class="form-label" for="current_password">Current password</label><input class="form-control" id="current_password" name="current_password" type="password" required autocomplete="current-password"></div>
<div><label class="form-label" for="new_password">New password (12 to 72 bytes)</label><input class="form-control" id="new_password" name="new_password" type="password" minlength="12" maxlength="72" required autocomplete="new-password"></div>
<div><label class="form-label" for="confirm_password">Confirm new password</label><input class="form-control" id="confirm_password" name="confirm_password" type="password" minlength="12" maxlength="72" required autocomplete="new-password"></div>
<button class="btn btn-primary">Update Password</button></form></main><?php require __DIR__ . '/../includes/footer.php'; ?>

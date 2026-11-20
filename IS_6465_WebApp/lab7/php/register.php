<?php
require_once __DIR__ . '/../config/db.php';
require_once __DIR__ . '/../services/userService.php';
require_once __DIR__ . '/../includes/auth.php';
startSecureSession();
$error = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    verifyCsrfToken($_POST);
    try {
        registerUser(openDatabase(), $_POST);
        $_SESSION['registration_success'] = 'Account created. You can now log in.';
        header('Location: login.php', true, 303); exit;
    } catch (InvalidArgumentException $e) { $error = $e->getMessage(); }
    catch (Throwable $e) { error_log($e->getMessage()); $error = 'Unable to create the account. Please check the details and try again.'; }
} elseif ($_SERVER['REQUEST_METHOD'] !== 'GET') { http_response_code(405); exit('Method not allowed'); }
require __DIR__ . '/../includes/header.php'; require __DIR__ . '/../includes/nav.php'; ?>
<main class="container py-4 form-container"><h1>Create an account</h1>
<?php if ($error): ?><div class="alert alert-danger"><?= htmlspecialchars($error, ENT_QUOTES, 'UTF-8') ?></div><?php endif; ?>
<form method="post" class="vstack gap-3" novalidate>
<input type="hidden" name="csrf_token" value="<?= htmlspecialchars(csrfToken(), ENT_QUOTES, 'UTF-8') ?>">
<div><label class="form-label" for="full_name">Full name</label><input class="form-control" id="full_name" name="full_name" maxlength="120" required value="<?= htmlspecialchars((string)($_POST['full_name'] ?? ''), ENT_QUOTES, 'UTF-8') ?>"></div>
<div><label class="form-label" for="email">Email</label><input class="form-control" id="email" name="email" type="email" maxlength="254" required value="<?= htmlspecialchars((string)($_POST['email'] ?? ''), ENT_QUOTES, 'UTF-8') ?>"></div>
<div><label class="form-label" for="password">Password (12 to 72 bytes)</label><input class="form-control" id="password" name="password" type="password" minlength="12" maxlength="72" required autocomplete="new-password"></div>
<div><label class="form-label" for="confirm_password">Confirm password</label><input class="form-control" id="confirm_password" name="confirm_password" type="password" minlength="12" maxlength="72" required autocomplete="new-password"></div>
<fieldset><legend>Account type</legend><label class="me-3"><input type="radio" name="role" value="Student" required <?= ($_POST['role'] ?? '') === 'Student' ? 'checked' : '' ?>> Student</label><label><input type="radio" name="role" value="Tutor" <?= ($_POST['role'] ?? '') === 'Tutor' ? 'checked' : '' ?>> Tutor</label></fieldset>
<p class="text-muted">Administrator accounts can only be assigned by an administrator.</p><button class="btn btn-primary">Create Account</button>
</form></main><?php require __DIR__ . '/../includes/footer.php'; ?>

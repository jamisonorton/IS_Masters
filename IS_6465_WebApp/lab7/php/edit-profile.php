<?php
require_once __DIR__ . '/../config/db.php'; require_once __DIR__ . '/../services/userService.php'; require_once __DIR__ . '/../includes/auth.php';
$pdo = openDatabase(); $user = requireLogin($pdo); $error = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    verifyCsrfToken($_POST);
    try { updateOwnProfile($pdo, $user['user_id'], $_POST['full_name'] ?? '', $_POST['email'] ?? ''); header('Location: profile.php?updated=1', true, 303); exit; }
    catch (InvalidArgumentException $e) { $error = $e->getMessage(); }
    catch (Throwable $e) { error_log($e->getMessage()); $error = 'Unable to save profile changes.'; }
} elseif ($_SERVER['REQUEST_METHOD'] !== 'GET') { http_response_code(405); exit('Method not allowed'); }
require __DIR__ . '/../includes/header.php'; require __DIR__ . '/../includes/nav.php'; ?>
<main class="container py-4 form-container"><h1>Edit Profile</h1>
<?php if ($error): ?><div class="alert alert-danger"><?= htmlspecialchars($error, ENT_QUOTES, 'UTF-8') ?></div><?php endif; ?>
<form method="post" class="vstack gap-3"><input type="hidden" name="csrf_token" value="<?= htmlspecialchars(csrfToken(), ENT_QUOTES, 'UTF-8') ?>">
<div><label class="form-label" for="full_name">Name</label><input class="form-control" id="full_name" name="full_name" required maxlength="120" value="<?= htmlspecialchars((string)($_POST['full_name'] ?? $user['full_name']), ENT_QUOTES, 'UTF-8') ?>"></div>
<div><label class="form-label" for="email">Email</label><input class="form-control" id="email" name="email" type="email" required maxlength="254" value="<?= htmlspecialchars((string)($_POST['email'] ?? $user['email']), ENT_QUOTES, 'UTF-8') ?>"></div>
<p>Role and status are managed separately and cannot be changed here.</p><button class="btn btn-primary">Save Changes</button> <a class="btn btn-secondary" href="profile.php">Cancel</a></form></main><?php require __DIR__ . '/../includes/footer.php'; ?>

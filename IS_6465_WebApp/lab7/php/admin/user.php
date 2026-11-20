<?php
require_once __DIR__ . '/../../config/db.php'; require_once __DIR__ . '/../../repositories/userPDO.php'; require_once __DIR__ . '/../../services/userService.php'; require_once __DIR__ . '/../../includes/auth.php';
$pdo = openDatabase(); $admin = requireLogin($pdo); requireRole($admin, ['Administrator']);
$id = filter_input(INPUT_GET, 'user_id', FILTER_VALIDATE_INT); if (!$id || $id < 1) { http_response_code(400); exit('Invalid account ID.'); }
$error = ''; $success = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    verifyCsrfToken($_POST);
    if (($_POST['confirmed'] ?? '') !== 'yes') $error = 'Confirm the selected account change before continuing.';
    else {
        try {
            switch ((string)($_POST['action'] ?? '')) {
                case 'role': changeUserRole($pdo, $id, (string)($_POST['role'] ?? '')); $success = 'Role updated.'; break;
                case 'status': changeUserStatus($pdo, $id, (string)($_POST['status'] ?? '')); $success = 'Account status updated.'; break;
                case 'delete': removeUserIfAllowed($pdo, $id); header('Location: users.php?deleted=1', true, 303); exit;
                default: throw new InvalidArgumentException('Choose a valid account action.');
            }
        } catch (InvalidArgumentException | DomainException $e) { $error = $e->getMessage(); }
        catch (Throwable $e) { error_log($e->getMessage()); $error = 'The account change could not be completed.'; }
    }
} elseif ($_SERVER['REQUEST_METHOD'] !== 'GET') { http_response_code(405); exit('Method not allowed'); }
$target = findUserById($pdo, $id); if (!$target) { http_response_code(404); exit('Account not found.'); }
$requestCount = userTutoringRequestCount($pdo, $id);
require __DIR__ . '/../../includes/header.php'; require __DIR__ . '/../../includes/nav.php'; ?>
<main class="container py-4"><p><a href="users.php">&larr; Manage Users</a></p><h1>Manage Account</h1>
<?php if ($error): ?><div class="alert alert-danger"><?= htmlspecialchars($error, ENT_QUOTES, 'UTF-8') ?></div><?php endif; ?>
<?php if ($success): ?><div class="alert alert-success"><?= htmlspecialchars($success, ENT_QUOTES, 'UTF-8') ?></div><?php endif; ?>
<dl class="row"><dt class="col-sm-3">Name</dt><dd class="col-sm-9"><?= htmlspecialchars($target['full_name'], ENT_QUOTES, 'UTF-8') ?></dd><dt class="col-sm-3">Email</dt><dd class="col-sm-9"><?= htmlspecialchars($target['email'], ENT_QUOTES, 'UTF-8') ?></dd><dt class="col-sm-3">Role</dt><dd class="col-sm-9"><?= htmlspecialchars($target['role'], ENT_QUOTES, 'UTF-8') ?></dd><dt class="col-sm-3">Status</dt><dd class="col-sm-9"><?= htmlspecialchars($target['status'], ENT_QUOTES, 'UTF-8') ?></dd><dt class="col-sm-3">Tutoring requests</dt><dd class="col-sm-9"><?= $requestCount ?></dd></dl>
<section class="card mb-3"><div class="card-body"><h2 class="h5">Update role</h2><form method="post" class="row g-2 align-items-end" onsubmit="return confirm('Save this account role?');"><input type="hidden" name="csrf_token" value="<?= htmlspecialchars(csrfToken(), ENT_QUOTES, 'UTF-8') ?>"><input type="hidden" name="action" value="role"><input type="hidden" name="confirmed" value="yes"><div class="col-md-5"><label class="form-label" for="role">New role</label><select class="form-select" name="role" id="role"><?php foreach (['Student','Tutor','Administrator'] as $value): ?><option value="<?= $value ?>" <?= $target['role'] === $value ? 'selected' : '' ?>><?= $value ?></option><?php endforeach; ?></select></div><div class="col-md-3"><button class="btn btn-primary">Save Role</button></div></form></div></section>
<section class="card mb-3"><div class="card-body"><h2 class="h5">Activate or deactivate</h2><form method="post" class="d-flex gap-2 align-items-center" onsubmit="return confirm('Apply this account status change?');"><input type="hidden" name="csrf_token" value="<?= htmlspecialchars(csrfToken(), ENT_QUOTES, 'UTF-8') ?>"><input type="hidden" name="action" value="status"><input type="hidden" name="confirmed" value="yes"><select class="form-select w-auto" name="status"><option value="Active" <?= $target['status'] === 'Active' ? 'selected' : '' ?>>Active</option><option value="Inactive" <?= $target['status'] === 'Inactive' ? 'selected' : '' ?>>Inactive</option></select><button class="btn btn-outline-primary">Confirm Status</button></form></div></section>
<section class="card border-danger"><div class="card-body"><h2 class="h5 text-danger">Delete account</h2><p>Deletion is blocked if this account has tutoring requests. Existing request records are retained.</p><form method="post" onsubmit="return confirm('Delete this user account? This cannot be undone.');"><input type="hidden" name="csrf_token" value="<?= htmlspecialchars(csrfToken(), ENT_QUOTES, 'UTF-8') ?>"><input type="hidden" name="action" value="delete"><input type="hidden" name="confirmed" value="yes"><button class="btn btn-danger">Confirm Delete Account</button></form></div></section>
</main><?php require __DIR__ . '/../../includes/footer.php'; ?>

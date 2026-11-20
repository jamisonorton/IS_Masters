<?php
require_once __DIR__ . '/../../config/db.php'; require_once __DIR__ . '/../../repositories/userPDO.php'; require_once __DIR__ . '/../../includes/auth.php';
$pdo = openDatabase(); $user = requireLogin($pdo); requireRole($user, ['Administrator']);
$search = trim((string)($_GET['search'] ?? '')); $role = (string)($_GET['role'] ?? ''); $status = (string)($_GET['status'] ?? '');
if (!in_array($role, ['', 'Student', 'Tutor', 'Administrator'], true) || !in_array($status, ['', 'Active', 'Inactive'], true)) { http_response_code(400); exit('Invalid filter.'); }
$users = searchUsers($pdo, $search, $role, $status);
require __DIR__ . '/../../includes/header.php'; require __DIR__ . '/../../includes/nav.php'; ?>
<main class="container py-4"><h1>Manage Users</h1>
<form method="get" class="row g-2 mb-4"><div class="col-md-5"><label class="visually-hidden" for="search">Search</label><input class="form-control" id="search" name="search" placeholder="Search name or email" value="<?= htmlspecialchars($search, ENT_QUOTES, 'UTF-8') ?>"></div>
<div class="col-md-3"><select class="form-select" name="role"><option value="">All roles</option><?php foreach (['Student','Tutor','Administrator'] as $value): ?><option <?= $role === $value ? 'selected' : '' ?>><?= $value ?></option><?php endforeach; ?></select></div>
<div class="col-md-2"><select class="form-select" name="status"><option value="">All statuses</option><?php foreach (['Active','Inactive'] as $value): ?><option <?= $status === $value ? 'selected' : '' ?>><?= $value ?></option><?php endforeach; ?></select></div><div class="col-md-2"><button class="btn btn-primary w-100">Search</button></div></form>
<?php if (!$users): ?><p>No accounts match these filters.</p><?php else: ?><div class="table-responsive"><table class="table"><thead><tr><th>Name</th><th>Email</th><th>Role</th><th>Status</th><th>Created</th><th></th></tr></thead><tbody>
<?php foreach ($users as $row): ?><tr><td><?= htmlspecialchars($row['full_name'], ENT_QUOTES, 'UTF-8') ?></td><td><?= htmlspecialchars($row['email'], ENT_QUOTES, 'UTF-8') ?></td><td><?= htmlspecialchars($row['role'], ENT_QUOTES, 'UTF-8') ?></td><td><?= htmlspecialchars($row['status'], ENT_QUOTES, 'UTF-8') ?></td><td><?= htmlspecialchars($row['created_at'], ENT_QUOTES, 'UTF-8') ?></td><td><a href="user.php?user_id=<?= (int)$row['user_id'] ?>">Manage</a></td></tr><?php endforeach; ?>
</tbody></table></div><?php endif; ?></main><?php require __DIR__ . '/../../includes/footer.php'; ?>

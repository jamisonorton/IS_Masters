<?php
require_once __DIR__ . '/../config/db.php'; require_once __DIR__ . '/../includes/auth.php';
$pdo = openDatabase(); $user = requireLogin($pdo);
require __DIR__ . '/../includes/header.php'; require __DIR__ . '/../includes/nav.php'; ?>
<main class="container py-4"><h1>My Profile</h1><dl class="row">
<dt class="col-sm-3">Name</dt><dd class="col-sm-9"><?= htmlspecialchars($user['full_name'], ENT_QUOTES, 'UTF-8') ?></dd>
<dt class="col-sm-3">Email</dt><dd class="col-sm-9"><?= htmlspecialchars($user['email'], ENT_QUOTES, 'UTF-8') ?></dd>
<dt class="col-sm-3">Role</dt><dd class="col-sm-9"><?= htmlspecialchars($user['role'], ENT_QUOTES, 'UTF-8') ?></dd>
<dt class="col-sm-3">Status</dt><dd class="col-sm-9"><?= htmlspecialchars($user['status'], ENT_QUOTES, 'UTF-8') ?></dd>
<dt class="col-sm-3">Created</dt><dd class="col-sm-9"><?= htmlspecialchars($user['created_at'], ENT_QUOTES, 'UTF-8') ?></dd>
</dl><a class="btn btn-primary" href="edit-profile.php">Edit Profile</a> <a class="btn btn-outline-secondary" href="change-password.php">Change Password</a>
<?php if ($user['role'] === 'Student'): ?> <a class="btn btn-outline-primary" href="requests.php">My Tutoring Requests</a><?php endif; ?></main><?php require __DIR__ . '/../includes/footer.php'; ?>

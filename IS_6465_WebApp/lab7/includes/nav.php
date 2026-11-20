<?php
require_once __DIR__ . '/auth.php';
startSecureSession();
$signedIn = !empty($_SESSION['user_id']);
?>
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
  <div class="container">
    <a class="navbar-brand" href="<?= htmlspecialchars(appUrl('index.php'), ENT_QUOTES, 'UTF-8') ?>">Peer Tutoring Hub</a>
    <div class="navbar-nav ms-auto align-items-lg-center">
      <?php if ($signedIn): ?>
        <a class="nav-link" href="<?= htmlspecialchars(appUrl('php/profile.php'), ENT_QUOTES, 'UTF-8') ?>">My Profile</a>
        <?php if (($_SESSION['role'] ?? '') === 'Student'): ?>
          <a class="nav-link" href="<?= htmlspecialchars(appUrl('php/requests.php'), ENT_QUOTES, 'UTF-8') ?>">My Requests</a>
          <a class="nav-link" href="<?= htmlspecialchars(appUrl('php/request-form.php'), ENT_QUOTES, 'UTF-8') ?>">Request a Session</a>
        <?php endif; ?>
        <?php if (($_SESSION['role'] ?? '') === 'Administrator'): ?>
          <a class="nav-link" href="<?= htmlspecialchars(appUrl('php/admin/users.php'), ENT_QUOTES, 'UTF-8') ?>">Manage Users</a>
          <a class="nav-link" href="<?= htmlspecialchars(appUrl('php/requests.php'), ENT_QUOTES, 'UTF-8') ?>">All Requests</a>
        <?php endif; ?>
        <form method="post" action="<?= htmlspecialchars(appUrl('php/logout.php'), ENT_QUOTES, 'UTF-8') ?>" class="ms-lg-2">
          <input type="hidden" name="csrf_token" value="<?= htmlspecialchars(csrfToken(), ENT_QUOTES, 'UTF-8') ?>">
          <button class="btn btn-sm btn-outline-light">Log Out</button>
        </form>
      <?php else: ?>
        <a class="nav-link" href="<?= htmlspecialchars(appUrl('php/login.php'), ENT_QUOTES, 'UTF-8') ?>">Log In</a>
        <a class="nav-link" href="<?= htmlspecialchars(appUrl('php/register.php'), ENT_QUOTES, 'UTF-8') ?>">Create Account</a>
      <?php endif; ?>
    </div>
  </div>
</nav>

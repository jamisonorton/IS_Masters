<?php
require_once __DIR__ . '/auth.php';
startSecureSession();
$signedIn = !empty($_SESSION['user_id']);
?>
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
  <div class="container">
    <a class="navbar-brand" href="/index.php">Peer Tutoring Hub</a>
    <div class="navbar-nav ms-auto align-items-lg-center">
      <?php if ($signedIn): ?>
        <a class="nav-link" href="/php/profile.php">My Profile</a>
        <?php if (($_SESSION['role'] ?? '') === 'Student'): ?>
          <a class="nav-link" href="/php/requests.php">My Requests</a>
          <a class="nav-link" href="/php/request-form.php">Request a Session</a>
        <?php endif; ?>
        <?php if (($_SESSION['role'] ?? '') === 'Administrator'): ?>
          <a class="nav-link" href="/php/admin/users.php">Manage Users</a>
          <a class="nav-link" href="/php/requests.php">All Requests</a>
        <?php endif; ?>
        <form method="post" action="/php/logout.php" class="ms-lg-2">
          <input type="hidden" name="csrf_token" value="<?= htmlspecialchars(csrfToken(), ENT_QUOTES, 'UTF-8') ?>">
          <button class="btn btn-sm btn-outline-light">Log Out</button>
        </form>
      <?php else: ?>
        <a class="nav-link" href="/php/login.php">Log In</a>
        <a class="nav-link" href="/php/register.php">Create Account</a>
      <?php endif; ?>
    </div>
  </div>
</nav>

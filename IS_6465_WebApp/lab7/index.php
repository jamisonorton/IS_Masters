<?php
require_once __DIR__ . '/config/db.php';
require_once __DIR__ . '/includes/auth.php';
startSecureSession();
header('Location: ' . (empty($_SESSION['user_id']) ? '/php/login.php' : '/php/profile.php'), true, 303);
exit;

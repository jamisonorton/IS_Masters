<?php
require_once __DIR__ . '/../config/db.php'; require_once __DIR__ . '/../services/requestService.php'; require_once __DIR__ . '/../includes/auth.php';
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); exit('POST required'); }
verifyCsrfToken($_POST);
$pdo = openDatabase(); $user = requireLogin($pdo); requireRole($user, ['Student']);
$input = $_POST; $input['student_name'] = $user['full_name']; $input['student_email'] = $user['email']; $input['user_id'] = $user['user_id'];
try { $id = submitRequest($pdo, $input); header('Location: request-details.php?request_id=' . $id, true, 303); exit; }
catch (InvalidArgumentException $e) { http_response_code(422); $message = $e->getMessage(); }
catch (Throwable $e) { error_log($e->getMessage()); http_response_code(500); $message = 'Unable to save the request.'; }
require __DIR__ . '/../includes/header.php'; require __DIR__ . '/../includes/nav.php'; ?>
<main class="container py-4"><h1>Request could not be submitted</h1><p><?= htmlspecialchars($message, ENT_QUOTES, 'UTF-8') ?></p><a href="request-form.php">Return to form</a></main><?php require __DIR__ . '/../includes/footer.php'; ?>

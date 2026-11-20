<?php
require_once __DIR__ . '/../config/db.php'; require_once __DIR__ . '/../services/requestService.php'; require_once __DIR__ . '/../includes/auth.php';
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); exit('POST required'); }
verifyCsrfToken($_POST); $pdo = openDatabase(); $user = requireLogin($pdo); requireRole($user, ['Student', 'Administrator']);
$id = filter_input(INPUT_POST, 'request_id', FILTER_VALIDATE_INT); if (!$id || $id < 1) { http_response_code(400); exit('Invalid ID'); }
try {
    $ok = reviseRequest($pdo, $id, $_POST, $user['user_id'], $user['role'] === 'Administrator');
    if (!$ok) { http_response_code(404); exit('Request not found or not editable.'); }
    header('Location: request-details.php?request_id=' . $id, true, 303); exit;
} catch (InvalidArgumentException $e) { http_response_code(422); $message = $e->getMessage(); }
catch (Throwable $e) { error_log($e->getMessage()); http_response_code(500); $message = 'Unable to update the request.'; }
require __DIR__ . '/../includes/header.php'; require __DIR__ . '/../includes/nav.php'; ?><main class="container py-4"><h1>Request could not be updated</h1><p><?= htmlspecialchars($message, ENT_QUOTES, 'UTF-8') ?></p><a href="edit-request.php?request_id=<?= (int)$id ?>">Return to request</a></main><?php require __DIR__ . '/../includes/footer.php'; ?>

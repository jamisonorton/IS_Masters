<?php
require_once __DIR__ . '/../config/db.php'; require_once __DIR__ . '/../repositories/requestPDO.php'; require_once __DIR__ . '/../includes/auth.php';
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); exit('POST required'); }
verifyCsrfToken($_POST); $pdo = openDatabase(); $user = requireLogin($pdo); requireRole($user, ['Student', 'Administrator']);
$id = filter_input(INPUT_POST, 'request_id', FILTER_VALIDATE_INT); if (!$id || $id < 1) { http_response_code(400); exit('Invalid ID'); }
try {
    $ok = cancelOpenRequest($pdo, $id, $user['user_id'], $user['role'] === 'Administrator');
    if (!$ok) { http_response_code(404); exit('Request not found or not open.'); }
    header('Location: request-details.php?request_id=' . $id, true, 303); exit;
} catch (Throwable $e) { error_log($e->getMessage()); http_response_code(500); exit('Unable to cancel the request.'); }

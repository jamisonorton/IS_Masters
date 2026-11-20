<?php
require_once __DIR__ . '/../config/db.php'; require_once __DIR__ . '/../repositories/requestPDO.php'; require_once __DIR__ . '/../services/requestService.php'; require_once __DIR__ . '/../includes/auth.php';
$pdo = openDatabase(); $user = requireLogin($pdo); requireRole($user, ['Student', 'Administrator']);
$id = filter_input(INPUT_GET, 'request_id', FILTER_VALIDATE_INT); if (!$id || $id < 1) { http_response_code(400); exit('Invalid request ID'); }
$isAdmin = $user['role'] === 'Administrator'; $r = findRequestForUser($pdo, $id, $user['user_id'], $isAdmin);
if (!$r) { http_response_code(404); exit('Request not found.'); }
$topic = decodeTopic($r['topic']); require __DIR__ . '/../includes/header.php'; require __DIR__ . '/../includes/nav.php'; ?>
<main class="container py-4"><h1>Request #<?= (int)$id ?></h1><dl>
<?php if ($isAdmin): ?><dt>Student</dt><dd><?= htmlspecialchars($r['student_name'], ENT_QUOTES, 'UTF-8') ?></dd><?php endif; ?>
<dt>Course</dt><dd><?= htmlspecialchars($r['course'], ENT_QUOTES, 'UTF-8') ?></dd><dt>Request details</dt><dd><?= htmlspecialchars($topic['reason'], ENT_QUOTES, 'UTF-8') ?></dd><dt>Topics</dt><dd><?= htmlspecialchars(implode(', ', $topic['topics']), ENT_QUOTES, 'UTF-8') ?></dd><dt>Preferred date</dt><dd><?= htmlspecialchars($r['preferred_date'], ENT_QUOTES, 'UTF-8') ?></dd><dt>Preferred time</dt><dd><?= htmlspecialchars($r['preferred_time'], ENT_QUOTES, 'UTF-8') ?></dd><dt>Status</dt><dd><?= htmlspecialchars($r['status'], ENT_QUOTES, 'UTF-8') ?></dd></dl>
<?php if ($r['status'] === 'Open'): ?><a class="btn btn-primary" href="edit-request.php?request_id=<?= (int)$id ?>">Edit</a> <form method="post" action="delete-request.php" class="d-inline" onsubmit="return confirm('Cancel this open request?');"><input type="hidden" name="request_id" value="<?= (int)$id ?>"><input type="hidden" name="csrf_token" value="<?= htmlspecialchars(csrfToken(), ENT_QUOTES, 'UTF-8') ?>"><button class="btn btn-outline-danger">Cancel request</button></form><?php endif; ?> <a href="requests.php" class="btn btn-secondary">Back to requests</a></main><?php require __DIR__ . '/../includes/footer.php'; ?>

<?php
require_once __DIR__ . '/../config/db.php'; require_once __DIR__ . '/../repositories/requestPDO.php'; require_once __DIR__ . '/../services/requestService.php'; require_once __DIR__ . '/../includes/auth.php';
$pdo = openDatabase(); $user = requireLogin($pdo); requireRole($user, ['Student', 'Administrator']);
$id = filter_input(INPUT_GET, 'request_id', FILTER_VALIDATE_INT); if (!$id || $id < 1) { http_response_code(400); exit('Invalid request ID'); }
$r = findRequestForUser($pdo, $id, $user['user_id'], $user['role'] === 'Administrator'); if (!$r) { http_response_code(404); exit('Request not found.'); }
$topic = decodeTopic($r['topic']); require __DIR__ . '/../includes/header.php'; require __DIR__ . '/../includes/nav.php'; ?>
<main class="container py-4"><h1>Edit request #<?= (int)$id ?></h1>
<?php if ($r['status'] !== 'Open'): ?><p>Only Open requests may be edited.</p><?php else: ?>
<form method="post" action="update-request.php"><input type="hidden" name="csrf_token" value="<?= htmlspecialchars(csrfToken(), ENT_QUOTES, 'UTF-8') ?>"><input type="hidden" name="request_id" value="<?= (int)$id ?>">
<label class="form-label" for="course">Course</label><select class="form-select mb-3" id="course" name="course"><?php foreach (['IS 6465','IS 6495','IS 6570'] as $c): ?><option value="<?= htmlspecialchars($c, ENT_QUOTES, 'UTF-8') ?>" <?= $c === $r['course'] ? 'selected' : '' ?>><?= htmlspecialchars($c, ENT_QUOTES, 'UTF-8') ?></option><?php endforeach; ?></select>
<label class="form-label" for="reason">What would you like help with?</label><textarea class="form-control mb-3" id="reason" name="reason" minlength="10" maxlength="500" required><?= htmlspecialchars($topic['reason'], ENT_QUOTES, 'UTF-8') ?></textarea>
<label class="form-label" for="preferreddate">Preferred date</label><input class="form-control mb-3" id="preferreddate" name="preferreddate" type="date" value="<?= htmlspecialchars($r['preferred_date'], ENT_QUOTES, 'UTF-8') ?>" required>
<fieldset><legend>Topics</legend><?php foreach (['Exam review','Practice problems','Study plan'] as $t): ?><label class="me-3"><input type="checkbox" name="topics[]" value="<?= htmlspecialchars($t, ENT_QUOTES, 'UTF-8') ?>" <?= in_array($t, $topic['topics'], true) ? 'checked' : '' ?>> <?= htmlspecialchars($t, ENT_QUOTES, 'UTF-8') ?></label><?php endforeach; ?></fieldset>
<fieldset><legend>Preferred time</legend><?php foreach (['Morning','Afternoon','Evening'] as $t): ?><label class="me-3"><input type="radio" name="preferredtime" value="<?= $t ?>" <?= $t === $r['preferred_time'] ? 'checked' : '' ?> required> <?= $t ?></label><?php endforeach; ?></fieldset>
<button class="btn btn-primary mt-3">Save changes</button> <a class="btn btn-secondary mt-3" href="request-details.php?request_id=<?= (int)$id ?>">Back</a></form><?php endif; ?></main><?php require __DIR__ . '/../includes/footer.php'; ?>

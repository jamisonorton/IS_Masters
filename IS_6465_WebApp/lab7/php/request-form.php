<?php
require_once __DIR__ . '/../config/db.php'; require_once __DIR__ . '/../includes/auth.php';
$pdo = openDatabase(); $user = requireLogin($pdo); requireRole($user, ['Student']);
require __DIR__ . '/../includes/header.php'; require __DIR__ . '/../includes/nav.php'; ?>
<main class="container py-4"><h1>Request a tutoring session</h1>
<form class="tutoring-request-form" action="process-request.php" method="post"><input type="hidden" name="csrf_token" value="<?= htmlspecialchars(csrfToken(), ENT_QUOTES, 'UTF-8') ?>">
<div class="form-field"><label for="student_name">Student name</label><input id="student_name" value="<?= htmlspecialchars($user['full_name'], ENT_QUOTES, 'UTF-8') ?>" readonly></div>
<div class="form-field"><label for="student_email">Student email</label><input id="student_email" value="<?= htmlspecialchars($user['email'], ENT_QUOTES, 'UTF-8') ?>" readonly></div>
<div class="form-field"><label for="course">Course</label><select id="course" name="course" required><option value="">Choose a course</option><option>IS 6465</option><option>IS 6495</option><option>IS 6570</option></select></div>
<div class="form-field"><label for="preferreddate">Preferred date</label><input id="preferreddate" name="preferreddate" type="date" required></div>
<div class="form-field form-field-full"><label for="reason">What would you like help with?</label><textarea id="reason" name="reason" rows="4" minlength="10" maxlength="500" required></textarea></div>
<fieldset><legend>Topics</legend><?php foreach (['Exam review','Practice problems','Study plan'] as $topic): ?><label class="choice"><input type="checkbox" name="topics[]" value="<?= htmlspecialchars($topic, ENT_QUOTES, 'UTF-8') ?>"><span><?= htmlspecialchars($topic, ENT_QUOTES, 'UTF-8') ?></span></label><?php endforeach; ?></fieldset>
<fieldset><legend>Preferred time</legend><?php foreach (['Morning','Afternoon','Evening'] as $time): ?><label class="choice"><input type="radio" name="preferredtime" value="<?= $time ?>" required><span><?= $time ?></span></label><?php endforeach; ?></fieldset>
<button type="submit">Request session</button></form></main><?php require __DIR__ . '/../includes/footer.php'; ?>

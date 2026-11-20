<?php
function findStudentByEmail($pdo, $email)
{
    $stmt = $pdo->prepare('SELECT student_id, student_name, student_email, user_id FROM students WHERE student_email = ?');
    $stmt->execute([$email]);
    return $stmt->fetch();
}

function findStudentByUserId($pdo, $userId)
{
    $stmt = $pdo->prepare('SELECT student_id, student_name, student_email, user_id FROM students WHERE user_id = ?');
    $stmt->execute([(int)$userId]);
    return $stmt->fetch();
}

function insertStudentIfAbsent($pdo, $name, $email)
{
    $stmt = $pdo->prepare('INSERT OR IGNORE INTO students(student_name,student_email) VALUES(?,?)');
    $stmt->execute([$name, $email]);
}

function linkStudentToUser($pdo, $name, $email, $userId)
{
    insertStudentIfAbsent($pdo, $name, $email);
    $student = findStudentByEmail($pdo, $email);
    if (!$student) throw new RuntimeException('Student record could not be created.');
    if ($student['user_id'] !== null && (int)$student['user_id'] !== (int)$userId) {
        throw new DomainException('That email is already linked to another account.');
    }
    $stmt = $pdo->prepare('UPDATE students SET student_name = ?, user_id = ? WHERE student_id = ?');
    $stmt->execute([$name, (int)$userId, (int)$student['student_id']]);
    return (int)$student['student_id'];
}

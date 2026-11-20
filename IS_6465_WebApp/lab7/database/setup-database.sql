-- Lab 6 baseline schema. Run upgrade-to-user-management.sql afterward.
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    student_email TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS tutoring_requests (
    request_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course TEXT NOT NULL,
    topic TEXT NOT NULL,
    preferred_date TEXT NOT NULL,
    preferred_time TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Open'
        CHECK (status IN ('Open', 'Cancelled', 'Assigned', 'Completed')),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

INSERT OR IGNORE INTO students (student_name, student_email)
VALUES ('Maria Lopez', 'maria.lopez@example.com');

INSERT INTO tutoring_requests
    (student_id, course, topic, preferred_date, preferred_time)
SELECT 1, 'IS 6465', 'PHP arrays and forms', '2026-11-03', 'Afternoon'
WHERE EXISTS (SELECT 1 FROM students WHERE student_id = 1)
  AND NOT EXISTS (
      SELECT 1 FROM tutoring_requests
      WHERE student_id = 1
        AND course = 'IS 6465'
        AND topic = 'PHP arrays and forms'
        AND preferred_date = '2026-11-03'
        AND preferred_time = 'Afternoon'
  );

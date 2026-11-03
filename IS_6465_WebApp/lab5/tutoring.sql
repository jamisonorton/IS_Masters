CREATE TABLE if not exists students (
    student_id INTEGER PRIMARY KEY,
    student_name TEXT NOT NULL,
    student_email TEXT NOT NULL UNIQUE
);

CREATE TABLE if not exists tutoring_requests (
    request_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course TEXT NOT NULL,
    topic TEXT NOT NULL,
    preferred_date TEXT NOT NULL,
    preferred_time TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Open',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students (student_id)
);

INSERT
    OR ignore INTO students (student_name, student_email)
VALUES (
        'Maria Lopez',
        'maria.lopez@example.com'
    );

INSERT
    OR ignore INTO tutoring_requests (
        student_id,
        course,
        topic,
        preferred_date,
        preferred_time
    )
VALUES (
        1,
        'IS 6465',
        'PHP arrays and forms',
        '2026-11-03',
        '14:00'
    );

INSERT
    OR ignore INTO students (student_name, student_email)
VALUES (
        'Jordan Lee',
        'jordan.lee@example.edu'
    );

INSERT
    OR ignore INTO tutoring_requests (
        student_id,
        course,
        topic,
        preferred_date,
        preferred_time
    )
VALUES (
        2,
        'IS 6465',
        'Forms',
        '2026-11-15',
        '14:00'
    );

INSERT
    OR ignore INTO tutoring_requests (
        student_id,
        course,
        topic,
        preferred_date,
        preferred_time
    )
VALUES (
        2,
        'IS 6465',
        'SQL SEELECT',
        '2026-11-12',
        '14:00'
    );

INSERT
    OR ignore INTO students (student_name, student_email)
VALUES (
        'Avery Patel',
        'avery.patel@example.edu'
    );

INSERT
    OR ignore INTO tutoring_requests (
        student_id,
        course,
        topic,
        preferred_date,
        preferred_time
    )
VALUES (
        3,
        'IS 6465',
        'SQlite CRUD',
        '2026-11-21',
        '01:00'
    );
-- Part 3: Read the stored data
SELECT * FROM students;

SELECT * FROM tutoring_requests;

SELECT *
FROM tutoring_requests
WHERE status = 'Open';

SELECT *
FROM tutoring_requests
WHERE request_id = 2;

SELECT
    tr.request_id,
    s.student_name,
    s.student_email,
    tr.course,
    tr.topic,
    tr.preferred_date,
    tr.preferred_time,
    tr.status
FROM tutoring_requests AS tr
JOIN students AS s
    ON tr.student_id = s.student_id
ORDER BY tr.preferred_date;

-- Part 4: Update one of Jordan's open requests and cancel Avery's request.
-- Request 3 belongs to Jordan; Avery's request_id is 4 in this database.
SELECT
    tr.request_id,
    s.student_name,
    tr.topic,
    tr.preferred_date,
    tr.preferred_time,
    tr.status
FROM tutoring_requests AS tr
JOIN students AS s
    ON tr.student_id = s.student_id
WHERE tr.request_id = 2;

SELECT
    tr.request_id,
    s.student_name,
    tr.topic,
    tr.preferred_date,
    tr.preferred_time,
    tr.status
FROM tutoring_requests AS tr
JOIN students AS s
    ON tr.student_id = s.student_id
WHERE s.student_name = 'Avery Patel';

UPDATE tutoring_requests
SET topic = 'PHP arrays and forms - updated',
    preferred_date = '2026-10-12',
    preferred_time = '15:00'
WHERE request_id = 2;

SELECT changes() AS jordan_rows_changed;

UPDATE tutoring_requests
SET status = 'Cancelled'
WHERE request_id = 4;

SELECT changes() AS avery_rows_changed;

SELECT
    tr.request_id,
    s.student_name,
    tr.topic,
    tr.preferred_date,
    tr.preferred_time,
    tr.status
FROM tutoring_requests AS tr
JOIN students AS s
    ON tr.student_id = s.student_id
WHERE tr.request_id = 2;

SELECT
    tr.request_id,
    s.student_name,
    tr.topic,
    tr.preferred_date,
    tr.preferred_time,
    tr.status
FROM tutoring_requests AS tr
JOIN students AS s
    ON tr.student_id = s.student_id
WHERE s.student_name = 'Avery Patel';

-- Part 5: Insert and delete a clearly identified test request.
INSERT INTO tutoring_requests (
    student_id,
    course,
    topic,
    preferred_date,
    preferred_time
)
VALUES (
    2,
    'IS 6465',
    'Delete Practice',
    '2026-11-03',
    '12:00'
);

SELECT last_insert_rowid() AS test_request_id;

SELECT request_id, student_id, course, topic, preferred_date, preferred_time, status
FROM tutoring_requests
WHERE topic = 'Delete Practice';

DELETE FROM tutoring_requests
WHERE request_id = 5;

SELECT changes() AS rows_deleted;

SELECT COUNT(*) AS test_rows_remaining
FROM tutoring_requests
WHERE request_id = 5;

SELECT
    request_id,
    student_id,
    course,
    topic,
    preferred_date,
    preferred_time,
    status
FROM tutoring_requests
ORDER BY request_id;

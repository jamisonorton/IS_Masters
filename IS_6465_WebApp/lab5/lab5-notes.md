# Lab 5 Notes: Table Schemas

# Part 1: Create the database tables

The database contains two tables: `students` and `tutoring_requests`.

```sql
CREATE TABLE students (
  student_id INTEGER PRIMARY KEY,
  student_name TEXT NOT NULL,
  student_email TEXT NOT NULL UNIQUE
);

CREATE TABLE tutoring_requests (
  request_id INTEGER PRIMARY KEY,
  student_id INTEGER NOT NULL,
  course TEXT NOT NULL,
  topic TEXT NOT NULL,
  preferred_date TEXT NOT NULL,
  preferred_time TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'Open',
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (student_id) REFERENCES students(student_id)
);
```

## Answers

1. **Primary keys:** `students.student_id` is the primary key for `students`. `tutoring_requests.request_id` is the primary key for `tutoring_requests`. Each uniquely identifies a row in its table.

2. **Foreign key and relationship:** `tutoring_requests.student_id` is a foreign key that references `students.student_id`. It connects each tutoring request to the student who submitted it. One student can have multiple tutoring requests, while each request refers to one student.

3. **Why `student_email` is `UNIQUE`:** The `UNIQUE` constraint prevents two student records from having the same email address. This helps keep student email addresses distinct in the database.

# Part 2: Insert students and tutoring requests

These are the `INSERT OR IGNORE` statements shown in the lab SQL screenshot. The database supplies each row's primary key and the default `status` and `created_at` values.

```sql
INSERT OR IGNORE INTO students (student_name, student_email)
VALUES ('Jordan Lee', 'jordan.lee@example.edu');

INSERT OR IGNORE INTO tutoring_requests (
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

INSERT OR IGNORE INTO tutoring_requests (
  student_id,
  course,
  topic,
  preferred_date,
  preferred_time
)
VALUES (
  2,
  'IS 6465',
  'SQL SELECT',
  '2026-11-12',
  '14:00'
);

INSERT OR IGNORE INTO students (student_name, student_email)
VALUES ('Avery Patel', 'avery.patel@example.edu');

INSERT OR IGNORE INTO tutoring_requests (
  student_id,
  course,
  topic,
  preferred_date,
  preferred_time
)
VALUES (
  3,
  'IS 6465',
  'SQLite CRUD',
  '2026-11-21',
  '01:00'
);
```

## `SELECT *` output

```text
sqlite> SELECT * FROM students;
1|Maria Lopez|maria.lopez@example.com
2|Jordan Lee|jordan.lee@example.edu
3|Avery Patel|avery.patel@example.edu

sqlite> SELECT * FROM tutoring_requests;
1|1|IS 6465|PHP arrays and forms - updated|2026-10-12|15:00|Cancelled|2026-11-03 17:24:51
2|2|IS 6465|Forms|2026-11-15|14:00|Open|2026-11-03 17:41:23
3|2|IS 6465|SQL SELECT|2026-11-12|14:00|Open|2026-11-03 17:41:24
4|3|IS 6465|SQLite CRUD|2026-11-21|01:00|Open|2026-11-03 17:42:17
```

The columns in the `students` output are `student_id`, `student_name`, and `student_email`. The `tutoring_requests` output columns are `request_id`, `student_id`, `course`, `topic`, `preferred_date`, `preferred_time`, `status`, and `created_at`.

## Why Jordan has one student row and two request rows

Jordan appears once in `students` because a student is stored once and identified by `student_id` (2). Jordan has two tutoring requests because each request is a separate row in `tutoring_requests`; both rows use `student_id` 2 to link back to Jordan. This is the one-to-many relationship: one student can submit multiple tutoring requests. The `INSERT OR IGNORE` statement also means a repeat insert for Jordan's already-used unique email is ignored rather than creating another student row.


# Part 3: Read the stored data

I ran the five requested queries against `tutoring.db`: all students, all tutoring requests, open requests only, the request with `request_id = 2`, and the joined request list below.

### JOIN query

```sql
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
JOIN students AS s ON tr.student_id = s.student_id
ORDER BY tr.preferred_date;
```

### JOIN query output

```text
request_id  student_name  student_email            course   topic                           preferred_date  preferred_time  status
----------  ------------  -----------------------  -------  ------------------------------  --------------  --------------  ---------
1           Maria Lopez   maria.lopez@example.com  IS 6465  PHP arrays and forms - updated  2026-10-12      15:00           Cancelled
3           Jordan Lee    jordan.lee@example.edu   IS 6465  SQL SEELECT                     2026-11-12      14:00           Open
2           Jordan Lee    jordan.lee@example.edu   IS 6465  Forms                           2026-11-15      14:00           Open
4           Avery Patel   avery.patel@example.edu  IS 6465  SQlite CRUD                     2026-11-21      01:00           Open
```

### Questions

1. **What does the `JOIN` condition connect?** It matches `tutoring_requests.student_id` with `students.student_id`, so each request is shown alongside the name and email of the student it belongs to.

2. **What is the difference between `JOIN` and `WHERE`?** `JOIN` combines related rows from tables using a matching condition. `WHERE` filters the resulting rows to keep only those that meet a condition, such as requests with `status = 'Open'`.

3. **Why retrieve one request by `request_id` instead of by topic alone?** `request_id` is the unique primary key for a request, so it identifies exactly one row. A topic can be shared by multiple requests, so searching by topic alone may return more than one row or the wrong request.


# Part 4: Update one request

I updated Jordan's open request with `request_id = 2`. In the current database, Avery's request is `request_id = 4` (request 3 belongs to Jordan), so I used ID 4 in the cancellation statement to update Avery's row only.

### UPDATE statements

```sql
UPDATE tutoring_requests
SET topic = 'PHP arrays and forms - updated',
    preferred_date = '2026-10-12',
    preferred_time = '15:00'
WHERE request_id = 2;

UPDATE tutoring_requests
SET status = 'Cancelled'
WHERE request_id = 4;
```

Each statement changed one row.

### Jordan's request before the update

```text
request_id  student_name  topic  preferred_date  preferred_time  status
----------  ------------  -----  --------------  --------------  ------
2           Jordan Lee    Forms  2026-11-15      14:00           Open
```

### Jordan's request after the update

```text
request_id  student_name  topic                           preferred_date  preferred_time  status
----------  ------------  ------------------------------  --------------  --------------  ------
2           Jordan Lee    PHP arrays and forms - updated  2026-10-12      15:00           Open
```

### Avery's request before cancellation

```text
request_id  student_name  topic        preferred_date  preferred_time  status
----------  ------------  -----------  --------------  --------------  ------
4           Avery Patel   SQlite CRUD  2026-11-21      01:00           Open
```

### Avery's request after cancellation

```text
request_id  student_name  topic        preferred_date  preferred_time  status
----------  ------------  -----------  --------------  --------------  ---------
4           Avery Patel   SQlite CRUD  2026-11-21      01:00           Cancelled
```

### Questions

1. **Why is a specific `WHERE` clause essential in an `UPDATE` statement?** It limits the change to the intended row. Without a `WHERE` clause, the database would update every row in the table; a carefully chosen condition also helps prevent changing the wrong request.

2. **Why use `Cancelled` instead of immediately deleting a real request?** Keeping the row preserves a record of the request and its status. The hub can retain the history for tracking and reporting while making clear that the request is no longer active.

# Part 5: Delete one test request

I inserted a clearly labeled `Delete Practice` request for Jordan (`student_id = 2`). The database assigned it `request_id = 5`.

### INSERT statement

```sql
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
```

### DELETE statement

```sql
DELETE FROM tutoring_requests
WHERE request_id = 5;
```

### Verification output

After the deletion, I checked for the test request by its ID and listed the remaining requests. The count for request ID 5 is zero, and requests 1 through 4 remain.

```text
request_id  student_id  course   topic                           preferred_date  preferred_time  status
----------  ----------  -------  ------------------------------  --------------  --------------  ---------
1           1           IS 6465  PHP arrays and forms - updated  2026-10-12      15:00           Cancelled
2           2           IS 6465  PHP arrays and forms - updated  2026-10-12      15:00           Open
3           2           IS 6465  SQL SEELECT                     2026-11-12      14:00           Open
4           3           IS 6465  SQlite CRUD                     2026-11-21      01:00           Cancelled
```

The verification query for the deleted test row returned:

```text
test_rows_remaining
-------------------
0
```

### Question

**Why is a `WHERE` clause essential in a `DELETE` statement?** It limits the deletion to the intended row. Without a `WHERE` clause, the database would delete every row in the table. Using the unique `request_id` makes it clear which single request should be removed.

# Part 6: Reflect on the CRUD workflow

| CRUD action | SQL statement used in this lab | Peer Tutoring Hub example |
| ----------- | ------------------------------ | ------------------------- |
| Create | `INSERT INTO ... VALUES (...);` | Add a student or create a tutoring request. |
| Read | `SELECT ... FROM ...;` (including a `JOIN` for the request list) | Show students and requests, including each request's student's name and email. |
| Update | `UPDATE tutoring_requests SET ... WHERE request_id = ...;` | Change a request's details or mark it as cancelled. |
| Delete | `DELETE FROM tutoring_requests WHERE request_id = ...;` | Remove a specific test request during development. |

### Questions

1. **How does the database preserve the connection between a student and that student's requests?** Each request stores a `student_id` foreign key that references `students.student_id`. That link identifies which student submitted the request.

2. **Which database constraint prevents two student rows from using the same email address?** The `UNIQUE` constraint on `students.student_email`.

3. **What could happen if an `UPDATE` or `DELETE` statement did not include a `WHERE` clause?** An `UPDATE` could change every row in the table, and a `DELETE` could remove every row in the table.

4. **Why should PHP send HTML form values as parameters instead of placing them directly into SQL text?** Parameterized queries keep submitted values separate from the SQL instructions. This helps prevent SQL injection and handles values such as quotes safely.

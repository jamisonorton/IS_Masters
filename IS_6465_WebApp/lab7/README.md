# Peer Tutoring Hub — Lab 7 User Management

This package extends the supplied Lab 6 PHP, PDO, and SQLite application. It implements UM-01 through UM-10 and protects the existing tutoring request workflow with authentication, role checks, ownership rules, and CSRF protection.

## Run the application

Requirements: PHP 8.0 or later with PDO SQLite and mbstring enabled; SQLite 3 for the optional schema setup command.

1. From this `lab7` directory, run `sqlite3 database/tutoring.db < database/setup-database.sql` if you want to initialize or refresh the demo schema. The included database is the Lab 6 sample database. The app adds the user account table and a nullable `students.user_id` link when it opens the database, preserving existing students and tutoring requests.
2. Create the first administrator in a terminal: `php php/cli/create-admin.php`. The password is entered without terminal echo. This local CLI tool refuses to create another administrator while an active one exists. Public registration only permits Student and Tutor roles.
3. Start the local server from this directory: `php -S 0.0.0.0:8000 php/router.php`.
4. Open the forwarded application URL. Students and tutors can register. Sign in as the administrator to search and manage users.

Use HTTPS outside local development. Session cookies use `Secure` when PHP detects HTTPS, always use `HttpOnly`, and use `SameSite=Lax`.

## Architecture

- `php/` contains request handlers and pages.
- `includes/` contains shared navigation, validation, session, authorization, and CSRF helpers.
- `services/` coordinates account and tutoring workflows and validates submitted values.
- `repositories/` contains prepared PDO statements.
- `config/db.php` opens SQLite, enables foreign keys, and safely adds the user-management schema to the supplied Lab 6 database.
- `database/` contains the preserved sample database and setup SQL for a fresh database.
- `tests/` contains isolated CLI regression checks; tests use an in-memory SQLite database and do not write to `tutoring.db`.

The new `users` table is the authoritative account, role, and status record. `students.user_id` links a Student account to the original `students` entity; tutoring requests continue to use the existing `student_id` foreign key. Tutors can register and manage their profiles but have no tutoring-request workflow in this version. The Lab 6 topic checkboxes and reason textarea remain encoded in the existing `topic` text column as JSON.

## Security and business rules

- Passwords are hashed with `password_hash(PASSWORD_DEFAULT)` and verified with `password_verify`; new passwords must contain 12–72 bytes to prevent truncation with common default password algorithms.
- Login regenerates the session ID. Protected pages reload the current account and role from SQLite and end sessions after 20 minutes of inactivity.
- The session cookie contains only PHP's session identifier. The session stores user ID, display name, role, and activity time.
- Every state-changing form, including registration and logout, carries a random CSRF token verified with `hash_equals`.
- Students can submit and manage only their own Open requests. Queries and updates enforce ownership using the authenticated user ID. Administrators can view and manage all Open requests. Tutors are denied request access.
- Administrators can search accounts and change role or status. Public registration cannot create administrators. The last active administrator cannot be demoted, deactivated, or deleted.
- Account deletion is allowed only when the account has no tutoring requests. A related request blocks deletion so the request record is retained. This conservative rule resolves the design document's open deletion-policy question for this lab package.

## Tests

Run from this directory:

```sh
php tests/validation-tests.php
php tests/integration-tests.php
php tests/user-management-tests.php
```

The first two scripts retain the Lab 6 regression coverage; the new isolated harness covers account creation, hashing, login, profile and password updates, role and status rules, administrator safeguards, and account search. The scripts print individual PASS/FAIL checks and exit nonzero on a failure. They have not been run as part of generating this package.

## Requirement map

| Use case | Main implementation |
|---|---|
| UM-01 Create User Account | `php/register.php`, `services/userService.php::registerUser`, `repositories/userPDO.php::createUserRecord` |
| UM-02 View Own Account | `php/profile.php`, `includes/auth.php::requireLogin` |
| UM-03 View and Search User Accounts | `php/admin/users.php`, `php/admin/user.php`, `repositories/userPDO.php::searchUsers` |
| UM-04 Update Own Account | `php/edit-profile.php`, `services/userService.php::updateOwnProfile` |
| UM-05 Change Password | `php/change-password.php`, `services/userService.php::changeOwnPassword` |
| UM-06 Update User Role | `php/admin/user.php`, `services/userService.php::changeUserRole` |
| UM-07 Activate or Deactivate Account | `php/admin/user.php`, `services/userService.php::changeUserStatus` |
| UM-08 Delete User Account | `php/admin/user.php`, `services/userService.php::removeUserIfAllowed` |
| UM-09 Log In | `php/login.php`, `services/userService.php::authenticateUser` |
| UM-10 Log Out | `php/logout.php`, `includes/auth.php::logoutSession` |

## Traceability and verification status

All use cases have an implementation path in this package. See [TRACEABILITY.md](TRACEABILITY.md) for the requirement-to-file map and verification gaps. Runtime behavior remains **implemented, unverified** until the CLI scripts are run in the target PHP environment. The test suite does not claim execution evidence by existing on disk.

DROP TABLE if EXISTS depatment;

CREATE TABLE department(
    department_name VARCHAR(50) NOT NULL,
    department_number SMALLINT NOT NULL,
    manager_SSN VARCHAR(11),
    manager_start_date date,
);

INSERT INTO department VALUES ('R and D', 1, '123456789', '2016-02-20');

INSERT INTO department VALUES ('Finance', 2, '123456783', '2016-03-16');

INSERT INTO department (department_number, department_name, manager_SSN, manager_start_date) VALUES (3, 'Marketing', '123456788', '2016-05-20');

INSERT INTO department (department_number, department_name) VALUES (4, 'Human Resources');

SELECT * FROM department;
DROP TABLE if EXISTS employee;

CREATE TABLE employee (
    first_name VARCHAR(105) NOT NULL,
    middle_initial CHAR(1),
    last_name VARCHAR(105) NOT NULL,
    SSN VARCHAR(11) NOT NULL,
    DOB DATE NOT NULL,
    street_address VARCHAR(250),
    gender CHAR(1),
    salary MONEY,
    supervisor_SSN VARCHAR(11),
    department_number SMALLINT
);

EXEC sp_columns employee;

INSERT INTO employee VALUES ('Doug', 'E', 'Gilbert', '123456780', '1960-06-09', '300 south 200 west', 'M', 81200.05, '2223334444', 1);

INSERT INTO employee VALUES ('Amy', 'C', 'Elyot', '123456789','1973-03-26', '100 Main St.', 'F', 80000, NULL, 1);

INSERT INTO employee (first_name, last_name, SSN, supervisor_SSN, DOB, department_number) VALUES ('Richard', 'Smith', '987654321', '123456789', '1999-02-20', 1);

INSERT INTO employee (first_name, last_name, SSN, DOB) VALUES ('George', 'Haman', '123456783', '2001-06-25');

SELECT * FROM employee;
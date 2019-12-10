-- # Postgresql exercices source: https://www.w3resource.com/postgresql-exercises/

-- ## Basic select exercices

-- ### Exercice 1
SELECT first_name AS "First Name", last_name AS "Last Name"
FROM employees;

SELECT first_name "First Name", last_name "Last Name"
FROM employees;

-- ### Exercice 2
SELECT DISTINCT department_id FROM employees;

-- ### Exercice 3
SELECT * FROM employees ORDER BY first_name DESC;

-- ### Exercice 4
SELECT first_name, last_name, salary, 0.15*salary AS PF FROM employees;

-- ### Exercice 5
SELECT employee_id, first_name, last_name, salary
FROM employees ORDER BY salary;

SELECT employee_id, first_name, last_name, salary
FROM employees ORDER BY salary ASC;

-- ### Exercice 6
SELECT SUM(salary) total_salary FROM employees;

-- ### Exercice 7
SELECT MAX(salary) max_salary, MIN(salary) min_salary FROM employees;

-- ### Exercice 8
SELECT AVG(salary) avg_salary, COUNT(*) __count FROM employees;

-- ### Exercice 10
SELECT COUNT(DISTINCT(job_id)) FROM employees;

-- ### Exercice 11
SELECT UPPER(first_name) FROM employees;

-- ### Exercice 12
SELECT SUBSTRING(first_name,1,3) FROM employees;

-- ### Exercice 13
SELECT 171*214+625 result;

-- ### Exercice 14
SELECT CONCAT(first_name,' ', last_name) "Employee Name"
FROM employees;

-- ### Exercice 15
SELECT TRIM(first_name)
FROM employees;

-- ### Exercice 16
SELECT first_name,last_name,
LENGTH(first_name)+LENGTH(last_name)  "Length of  Names"
FROM employees;

-- ### Exercice 17
SELECT *
FROM employees
WHERE  first_name SIMILAR TO '%0|1|2|3|4|5|6|7|8|9%';

-- ### Exercice 18
SELECT * FROM employees LIMIT 10;

-- ### Exercice 19
SELECT first_name, last_name,
ROUND(salary/12,2) as "Monthly Salary"
FROM employees;

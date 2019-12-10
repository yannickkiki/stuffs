-- # Postgresql exercices source: https://www.w3resource.com/postgresql-exercises/

-- ## Basic Restricting and Sorting Data

-- ### Exercice 1
SELECT CONCAT(first_name, ' ', last_name) "name" , salary
FROM employees
WHERE salary NOT BETWEEN 10000 AND 15000;


-- ### Exercice 2
SELECT CONCAT(first_name, ' ', last_name) "name", department_id
FROM employees
WHERE department_id IN (30, 100)
ORDER BY department_id;


-- ### Exercice 3
SELECT CONCAT(first_name, ' ', last_name) "name", department_id
FROM employees
WHERE department_id IN (30, 100)
    AND salary NOT BETWEEN 10000 AND 15000
ORDER BY department_id;


-- ### Exercice 4
SELECT CONCAT(first_name, ' ', last_name) "name", hire_date
FROM employees
WHERE TO_CHAR(hire_date, 'YYYY') LIKE '%1987';


-- ### Exercice 5
SELECT first_name
FROM employees
WHERE first_name LIKE '%c%' AND first_name LIKE '%e%'
LIMIT 1;


-- ### Exercice 6
SELECT last_name, job_id, salary
FROM employees
WHERE job_id NOT IN ('IT_PROG', 'SH_CLERK')
    AND salary NOT IN (4500, 10000, 15000);


-- ### Exercice 7
-- Write a query to display the last names of employees whose name contain exactly six characters.
SELECT last_name
FROM employees
WHERE LENGTH(last_name) = 6;

SELECT last_name
FROM employees
WHERE last_name LIKE '______';


-- ### Exercice 8
SELECT last_name
FROM employees
WHERE last_name LIKE '__e%';


-- ### Exercice 9
SELECT DISTINCT('job_id') distinct_job_ids FROM employees;


-- ### Exercice 10
SELECT CONCAT(first_name, ' ', last_name) "name", salary, 0.15*salary pf
FROM employees;


-- ### Exercice 11
SELECT *
FROM employees
WHERE last_name IN ('Jones', 'Blake', 'Scott', 'King', 'Ford');

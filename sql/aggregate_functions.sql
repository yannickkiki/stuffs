-- # Postgresql exercices source: https://www.w3resource.com/postgresql-exercises/

-- ## Basic Aggregate Functions and Group by exercices

-- ### Exercice 1
SELECT COUNT(DISTINCT job_id) FROM employees;

-- ### Exercice 2
SELECT SUM(salary) FROM employees;

-- ### Exercice 3
SELECT MIN(salary) FROM employees;

-- ### Exercice 4
SELECT MAX(salary)
FROM employees
WHERE job_id = 'IT_PROG';

-- ### Exercice 5
SELECT AVG(salary), COUNT(*)
FROM employees
WHERE department_id = 90;

-- ### Exercice 6
SELECT MAX(salary), MIN(salary), SUM(salary), AVG(salary) FROM employees;

-- ### Exercice 7
SELECT job_id, COUNT(*)
FROM employees
GROUP BY job_id;

-- ### Exercice 8
SELECT MAX(salary) - MIN(salary) FROM employees;

-- ### Exercice 9
SELECT manager_id, MIN(salary)
FROM employees
WHERE manager_id IS NOT NULL
GROUP BY manager_id;

-- ### Exercice 10
SELECT department_id, SUM(salary)
FROM employees
GROUP BY department_id;

-- ### Exercice 11
SELECT job_id, AVG(salary)
FROM employees
WHERE job_id != 'IT_PROG'
GROUP BY job_id;
-- it seems that when you make a !=, it filter implicitly by the good type so null will be filtered
-- I was surprised that null values didn't came

-- ### Exercice 12
SELECT job_id, SUM(salary), MAX(salary), MIN(salary), AVG(salary)
FROM employees
WHERE department_id = 90
GROUP BY job_id;

-- ### Exercice 13
SELECT job_id, MAX(salary)
FROM employees
GROUP BY job_id
HAVING MAX(salary) >=4000;

-- ### Exercice 14
SELECT department_id, AVG(salary)
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 10;

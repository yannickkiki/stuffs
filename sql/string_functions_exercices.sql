-- # Postgresql exercices source: https://www.w3resource.com/postgresql-exercises/

-- ## String functions exercices

-- ### Exercice 1
-- Write a query to get the job_id and the ID(s) for those employees who is working in that post.
SELECT job_id, array_agg(employee_id)
FROM employees
GROUP BY job_id;

-- ### Exercice 2
-- Write a query to update the phone_number column with '999' where the substring '124' found in that column.
UPDATE employees
SET phone_number=REPLACE(phone_number, '124', '999')
WHERE phone_number LIKE '%124%';

-- ### Exercice 3
-- Write a query to find the details of those employees who contain eight or more characters in their first name.
SELECT * FROM employees
WHERE LENGTH(first_name) >= 8;

-- ### Exercice 4
-- Write a query to fill the maximum and
-- minimum salary with leading asterisks whether these two columns does not contain a seven digit number.
SELECT job_id, LPAD(trim(to_char(max_salary,'9999999')),7,'*') "Max Salary" ,
LPAD(trim(to_char(min_salary,'9999999')),7,'*') "Min Salary"
FROM jobs;

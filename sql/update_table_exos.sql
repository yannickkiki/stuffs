-- # Postgresql exercices source: https://www.w3resource.com/postgresql-exercises/

-- ## Update table exercices

-- ### Exercice 1
UPDATE employees SET email='not available';

-- ### Exercice 2
UPDATE employees SET email='not available', commission_pct=0.10;

-- ### Exercice 3
UPDATE employees SET email='not available', commission_pct=0.10
                WHERE department_id=110;

-- ### Exercice 4
UPDATE employees SET email='not available'
                WHERE department_id=80 AND commission_pct<0.2;

-- ### Exercice 5
UPDATE employees SET email='not available'
WHERE department_id=(SELECT department_id FROM department WHERE department_name='Accounting');

-- ### Exercice 6
UPDATE employees SET salary=8000
WHERE employee_id=105 AND salary<5000;

-- ### Exercice 7
UPDATE employees SET job_id='SH_CLERK'
WHERE employee_id=118 AND department_id=30 AND NOT job_id LIKE 'SH%';

-- ### Exercice 8
UPDATE employees SET salary=
    CASE department_id
        WHEN 40 THEN salary+(salary*.25)
        WHEN 90 THEN salary+(salary*.15)
        WHEN 110 THEN salary+(salary*.10)
        ELSE salary
    END;

<<<<<<< 7d7b3797e712139683354bc252c7bb08819db15c

UPDATE record SET unitssold_int = CAST( unitssold AS INTEGER);
UPDATE record SET columni_inti = floor(random() * 10)::int;
=======
UPDATE employees SET salary =
    CASE
      WHEN id < 3 THEN id*50000
      WHEN id=3 THEN id*60000
      ELSE id*70000
    END;
>>>>>>> - stuffs

-- # Postgresql exercices source: https://www.w3resource.com/postgresql-exercises/

-- ## Insert into exercices

-- ### Exercice 1
INSERT INTO countries(country_id, country_name, region_id)
    VALUES (1, 'Benin', 1);

-- ### Exercice 2
INSERT INTO countries(country_id, country_name)
    VALUES (2, 'France');

-- ### Exercice 3
CREATE TABLE country_new AS TABLE countries;

-- ### Exercice 4
INSERT INTO countries(country_id, country_name, region_id)
    VALUES (3, 'Canada', NULL);

-- ### Exercice 5
INSERT INTO countries(country_id, country_name, region_id)
    VALUES (4, 'Italy', 2), (5, 'Spain', 2), (6, 'Belgium', 2);

-- ### Exercice 6
INSERT INTO countries
SELECT * FROM country_new;

-- ### Exercice 7
INSERT INTO jobs VALUES (1, 'Software Engineer', 1000, 10000);

-- ### Exercice 9
CREATE TABLE countries (
    country_id SERIAL PRIMARY KEY,
    country_name varchar(40) NOT NULL,
    region_id integer NOT NULL,
    somefield SERIAL
);
INSERT INTO countries(country_name, region_id)
    VALUES ('Benin', 1);

-- ### Exercice 10
CREATE TABLE countries (
    country_id SERIAL PRIMARY KEY,
    country_name varchar(40) DEFAULT 'N/A',
    region_id integer NOT NULL,
    somefield SERIAL
);

-- ### Additionnal examples
INSERT INTO employee (first_name, last_name, salary)
    VALUES
       ('Yannick', 'KIKI', '132000'),
       ('Corentin', 'ALLOH', '156000')
);

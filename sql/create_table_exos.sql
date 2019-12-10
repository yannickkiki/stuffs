-- # Postgresql exercices source: https://www.w3resource.com/postgresql-exercises/

-- ## Create table exercices

-- ### Exercice 1

CREATE TABLE countries (
    country_id numeric(3,0),
    country_name varchar(45),
    region_id numeric(10,0)
);

SELECT * FROM countries;

SELECT * FROM information_schema.columns WHERE table_name = 'countries';

-- ### Exercice 3
CREATE TABLE dupl_countries AS
    (SELECT * FROM countries)
WITH NO DATA;

-- ### Exercice 4
CREATE TABLE dup_countries AS
    (SELECT * FROM countries)
;

CREATE TABLE dupp_countries AS
    TABLE countries
;

-- ### Exercice 5
DROP TABLE countries;
CREATE TABLE countries (
    country_id numeric(3),
    country_name varchar(45),
    region_id numeric(10) NOT NULL
);

-- ### Exercice 6
CREATE TABLE jobs (
    job_id numeric(10),
    job_title varchar(45),
    min_salary numeric(5),
    max_salary numeric(5) CHECK (max_salary <= 25000)
);
-- - psql show structure: \d jobs
INSERT INTO jobs (max_salary) VALUES (24000);
INSERT INTO jobs (max_salary) VALUES (26000);

-- ### Exercice 7
CREATE TABLE countries (
    country_id numeric(3),
    country_name varchar(45) CHECK(country_name IN ('Italy', 'India', 'China')),
    region_id numeric(10) NOT NULL
);

CREATE TABLE countries (
    country_id numeric(3),
    country_name varchar(45) CHECK(country_name IN ('Italy', 'India', 'China') OR country_name IN ('Italy', 'India', 'China')),
    region_id numeric(10) NOT NULL
);

-- ### Exercice 8
CREATE TABLE countries (
    country_id numeric(3),
    country_name varchar(45) UNIQUE,
    region_id numeric(10) NOT NULL
);

CREATE TABLE countries (
    country_id numeric(3),
    somefield numeric(5),
    country_name varchar(45),
    region_id numeric(10) NOT NULL,
    UNIQUE(country_id),
    UNIQUE(somefield)
);

CREATE TABLE countries (
    country_id numeric(3),
    somefield numeric(5),
    country_name varchar(45),
    region_id numeric(10) NOT NULL,
    UNIQUE(country_id,somefield)
);

-- ### Exercice 9
CREATE TABLE jobs (
    job_id numeric(10),
    job_title varchar(45) DEFAULT '',
    min_salary numeric(5) DEFAULT 8000,
    max_salary numeric(5)
);

-- ### Exercice 10
CREATE TABLE countries (
    country_id numeric(3) PRIMARY KEY,
    somefield numeric(5),
    country_name varchar(45),
    region_id numeric(10)
);

SELECT * FROM pg_indexes WHERE tablename = 'countries';

-- ### Exercice 11
CREATE TABLE countries (
    country_id SERIAL UNIQUE,
    somefield numeric(5),
    country_name varchar(45),
    region_id numeric(10)
);

-- ### Exercice 12
CREATE TABLE countries (
    country_id integer,
    somefield numeric(5),
    country_name varchar(45),
    region_id integer,
    UNIQUE(country_id, region_id)
);

-- ### Exercice 13
CREATE TABLE jobs (
    job_id numeric(10) UNIQUE,
    job_title varchar(45) DEFAULT '',
    min_salary numeric(5) DEFAULT 8000,
    max_salary numeric(5)
);

CREATE TABLE job_history (
    employee_id integer,
    start_date date,
    end_date date,
    some_date date DEFAULT CURRENT_DATE,
    job_id integer,
    department_id integer,
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
);

-- ### Exercice 14
CREATE TABLE department (
    department_id integer,
    manager_id integer,
    department_name varchar(45),
    location_id integer,
    PRIMARY KEY (department_id, manager_id)
);

CREATE TABLE employees (
    employee_id integer UNIQUE,
    first_name varchar(45),
    last_name varchar(45),
    email varchar(45),
    phone_number varchar(45),
    hire_date date,
    salary numeric(10),
    commission numeric(10),
    manager_id integer,
    department_id integer,
    FOREIGN KEY (manager_id, department_id) REFERENCES department(manager_id, department_id)
);

-- ### Exercice 16
CREATE TABLE employees (
    employee_id integer UNIQUE,
    first_name varchar(45),
    last_name varchar(45),
    job_id integer REFERENCES jobs(job_id),
    salary numeric(10,2)
);

CREATE TABLE employees (
    employee_id integer UNIQUE,
    first_name varchar(45),
    last_name varchar(45),
    job_id integer,
    salary numeric(10,2),
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- ### Exercice 17
CREATE TABLE employees (
    employee_id integer UNIQUE,
    first_name varchar(45),
    last_name varchar(45),
    job_id integer,
    salary numeric(10,2),
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
        ON UPDATE RESTRICT
        ON DELETE CASCADE
);

-- ### Exercice 18
CREATE TABLE employees (
    employee_id integer UNIQUE,
    first_name varchar(45),
    last_name varchar(45),
    job_id integer,
    salary numeric(10,2),
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
        ON UPDATE SET NULL
        ON DELETE SET NULL
);

-- Exercice 19
CREATE TABLE employees (
    employee_id integer UNIQUE,
    first_name varchar(45),
    last_name varchar(45),
    job_id integer,
    salary numeric(10,2),
    FOREIGN KEY (job_id) REFERENCES jobs(job_id)
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

-- ### Additionnal examples
CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    first_name varchar(255),
    last_name varchar(255),
    salary numeric(10, 2)
)

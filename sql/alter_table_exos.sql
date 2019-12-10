-- # Postgresql exercices source: https://www.w3resource.com/postgresql-exercises/

-- ## Alter table exercices

-- ### Exercice 1
ALTER TABLE countries RENAME TO countries_new;

-- ### Exercice 2
ALTER TABLE locations
ADD region_id integer;

ALTER TABLE locations
ADD region_id INT;

-- ### Exercice 3
ALTER TABLE locations
ALTER region_id TYPE text;

-- ### Exercice 4
ALTER TABLE locations
DROP country;

-- ### Exercice 5
-- - psql show structure: \d locations
ALTER TABLE locations
DROP state_province,
ADD state varchar(25);

-- ### Exercice 6
ALTER TABLE locations
ADD PRIMARY KEY (location_id);

-- ### Exercice 7
ALTER TABLE locations
ADD PRIMARY KEY (location_id, country_id);

-- ### Exercice 8
-- - psql show structure: \d locations
ALTER TABLE locations
DROP CONSTRAINT locations_pkey;

-- ### Exercice 9
ALTER TABLE job_history
ADD FOREIGN KEY (job_id) REFERENCES job(job_id);

-- ### Exercice 10
ALTER TABLE job_history
ADD CONSTRAINT fk_job_id FOREIGN KEY (job_id) REFERENCES job(job_id);

-- ### Exercice 11
ALTER TABLE job_history
DROP CONSTRAINT fk_job_id;

-- ### Exercice 12
CREATE UNIQUE INDEX index_job_id ON job_history(job_id);

ALTER TABLE job_history
ADD CONSTRAINT index_job_id PRIMARY KEY USING INDEX index_job_id;

-- ### Exercice 13
ALTER TABLE job_history
DROP CONSTRAINT index_job_id;


-- ### others
ALTER TABLE job ADD min_salary decimal(10, 2), ADD max_salary decimal(10, 2);

ALTER TABLE table_name
RENAME COLUMN column_name TO new_column_name;

ALTER TABLE queue ADD bro_id smallint;
ALTER TABLE queue ADD broco_id smallserial;

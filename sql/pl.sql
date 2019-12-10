-- 1
-- 1.1
CREATE FUNCTION jobs_total_max_salary() RETURNS bigint AS $$
DECLARE
    result integer;
BEGIN
    SELECT SUM(max_salary) INTO result FROM job;
    RETURN result;
END;
$$ LANGUAGE plpgsql;

-- 1.2
SELECT jobs_total_max_salary();


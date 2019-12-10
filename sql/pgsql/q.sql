SELECT id, row_number() over (order by id) as row_num FROM queue;

SELECT * FROM queue;

DELETE FROM queue WHERE id IN (
    SELECT id FROM
    (
        SELECT id, row_number() over (partition by (templet_id, email_id) order by id) AS row_num
        FROM queue
        WHERE scheduled IS NULL AND cancelled IS NULL
    ) q
    WHERE q.row_num > 1
);

ALTER TABLE queue ADD scheduled timestamp, ADD cancelled timestamp;

UPDATE queue
SET scheduled = now()
WHERE id = 7;

UPDATE queue
SET cancelled = now()
WHERE id = 8;

DROP TABLE queue;

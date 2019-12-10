SELECT
    tc.table_schema,
    tc.constraint_name,
    tc.table_name,
    kcu.column_name,
    ccu.table_schema AS foreign_table_schema,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name
FROM
    information_schema.table_constraints AS tc
    JOIN information_schema.key_column_usage AS kcu
      ON tc.constraint_name = kcu.constraint_name
      AND tc.table_schema = kcu.table_schema
    JOIN information_schema.constraint_column_usage AS ccu
      ON ccu.constraint_name = tc.constraint_name
      AND ccu.table_schema = tc.table_schema
WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name='mytable';

DELETE FROM queue WHERE id=2;

SELECT
   table_name,
   column_name,
   data_type
FROM
   information_schema.columns
WHERE
   table_name = 'campaign';

ALTER TABLE countries ALTER country_name TYPE integer;

ALTER TABLE countries ALTER country_name TYPE integer USING country_name::integer;

SELECT * FROM pg_indexes WHERE tablename = 'queue';

SELECT * FROM pg_indexes WHERE tablename = 'countries';

EXPLAIN SELECT id, columni_inti FROM record WHERE id < 1000;
EXPLAIN ANALYZE SELECT id, columni_inti FROM record WHERE id < 1000;

SELECT now() - CAST('1'||' DAYS' AS interval) , style->>'color_primary' FROM core.metacard;

SELECT EXISTS(SELECT NULL);
SELECT EXISTS(SELECT * FROM foxx.queue);
SELECT EXISTS(SELECT * FROM core.metacard);
SELECT EXISTS(
    SELECT 1 FROM radix.order WHERE radix.order.customer_id = radix.customer.id
);


-- accounts with no queue items
WITH existing_queue as (
    SELECT id, account_id
    FROM fresh_queue
)
SELECT *
FROM fresh_account
LEFT JOIN existing_queue ON fresh_account.id = existing_queue.account_id
WHERE existing_queue.id IS NULL

SELECT *
FROM fresh_account
WHERE id NOT IN (SELECT account_id FROM fresh_queue)

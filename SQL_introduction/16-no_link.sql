-- 16. No empty name
-- lists all records from second_table where name is not null
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
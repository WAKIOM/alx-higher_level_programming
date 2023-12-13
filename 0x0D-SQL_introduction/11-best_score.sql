-- list scores >= 10 ordered in descending order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

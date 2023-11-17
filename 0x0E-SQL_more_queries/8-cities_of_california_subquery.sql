-- Select cities of California
SELECT id, name
FROM cities
WHERE id IN (
	SELECT  id
	FROM states
	WHERE name = 'California'
);

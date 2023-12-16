-- Display count of records with a particular score
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score;

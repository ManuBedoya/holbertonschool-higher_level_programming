-- Ignoring the names = NULL and sorting for score
SELECT score, name FROM second_table WHERE name != "" ORDER BY score DESC;

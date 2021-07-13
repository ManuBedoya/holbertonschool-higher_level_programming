-- PRINT ALL CITIES
SELECT c.id, c.name, s.name FROM cities as c
INNER JOIN states as s
ON s.id = c.state_id;

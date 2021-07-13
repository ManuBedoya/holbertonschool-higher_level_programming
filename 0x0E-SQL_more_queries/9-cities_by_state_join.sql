-- PRINT ALL CITIES
SELECT cities.id, citites.name, states.name
FROM cities
INNER JOIN states
ON states.id = cities.state_id
ORDER BY cities.id ASC;

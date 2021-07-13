-- PRINT CITIES OF CALIFORNIA
SELECT c.id, c.name FROM states as s, cities as c
WHERE s.id = c.state_id
AND s.name = "California";

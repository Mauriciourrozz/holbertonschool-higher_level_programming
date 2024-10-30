-- Selecciona todas las ciudades de California que se pueden encontrar en la base de datos
SELECT *
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
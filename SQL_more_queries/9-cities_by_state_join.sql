-- Muestra las ciudades contenidas en la base de datos
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON states.state_id = cities.state_id
ORDER BY cities.id ASC;
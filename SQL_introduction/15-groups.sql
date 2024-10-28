-- Ennumera la cantidad de registros con el mismo score en la tabla second_table
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

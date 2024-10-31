-- Importar el volcado de la base de datos desde hbtn_0d_tvshows
SELECT tg.name AS name
FROM tv_genres tg
JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
JOIN tv_shows ts ON ts.id = tsg.show_id
WHERE ts.title = 'Dexter'
ORDER BY tg.name ASC;
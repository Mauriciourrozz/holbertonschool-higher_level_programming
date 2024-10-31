-- Importar el volcado de la base de datos desde hbtn_0d_tvshows
SELECT ts.title AS title
FROM tv_genres tg
JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
JOIN tv_shows ts ON ts.id = tsg.show_id
WHERE tg.name = 'Comedy'
ORDER BY ts.title ASC;
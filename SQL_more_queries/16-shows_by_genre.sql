-- Importar el volcado de la base de datos desde hbtn_0d_tvshows
SELECT ts.title AS title, tg.name AS name
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
LEFT JOIN tv_genres tg ON tsg.genre_id = tg.id
ORDER BY ts.title ASC, tg.name ASC;

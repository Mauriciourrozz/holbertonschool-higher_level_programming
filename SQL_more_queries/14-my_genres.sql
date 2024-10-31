-- Importar el volcado de la base de datos desde hbtn_0d_tvshows
SELECT tv_genre.name AS name
FROM tv_genres tv_genre
JOIN tv_show_genres tsg ON tv_genres.id = tsg.genre_id
JOIN tv_shows ts ON ts.id = tsg.show_id
WHERE ts.title = 'Dexter'
ORDER BY tv_genres.name ASC;
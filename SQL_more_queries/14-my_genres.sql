-- Importar el volcado de la base de datos desde hbtn_0d_tvshows
SELECT genres.name AS genre
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN genres ON tv_show_genres.genre_id = genres.id
WHERE tv_shows.name = 'Dexter';
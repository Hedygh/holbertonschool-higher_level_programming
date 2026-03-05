-- lists all genres not linked to the show Dexter
SELECT name
FROM tv_genres
WHERE id NOT IN (
    SELECT tv_show_genres.genre_id
    FROM tv_show_genres
    JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC;
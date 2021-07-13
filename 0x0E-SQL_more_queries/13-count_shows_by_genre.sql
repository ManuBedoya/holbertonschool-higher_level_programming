-- PRINT THE NUMBER OF SHOWS PER GENRE
SELECT tv_genres.name as genre, COUNT(tv_genres.name) number_of_shows
FROM ((
tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
)
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id)
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;

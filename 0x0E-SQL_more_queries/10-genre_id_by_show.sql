-- PRINT ALL SHOWS THAT COINTEINED AT LEAST ONE GENRE LINKED
SELECT ts.title, tsg.genre_id
FROM ((
tv_shows as ts
INNER JOIN tv_show_genres as tsg
ON ts.id = tsg.show_id
)
INNER JOIN tv_genres as tg
ON tsg.genre_id = tg.id)
ORDER BY ts.title;

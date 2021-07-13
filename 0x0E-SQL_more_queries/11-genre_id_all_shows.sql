-- PRINT ALL SHOWS
SELECT ts.title, tsg.genre_id
FROM tv_shows as ts
LEFT JOIN tv_show_genres as tsg
ON ts.id = tsg.show_id
ORDER BY ts.title;

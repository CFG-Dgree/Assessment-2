SELECT Movie_Name, Movie_Length
FROM movie_info
JOIN showings ON movie_info.Movie_ID = showings.Movie_ID
WHERE Start_Time > '12:00:00' AND Available_Seats > 0
ORDER BY Start_Time;

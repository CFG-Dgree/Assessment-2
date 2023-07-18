SELECT Movie_Name
FROM movie_info
WHERE Movie_ID = (
  SELECT Movie_ID
  FROM showings
  GROUP BY Movie_ID
  ORDER BY COUNT(*) DESC
  LIMIT 1
);

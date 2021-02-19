-- DROP TABLE youtubedata;
-- DROP TABLE imdbdata;

-- CREATE TABLE youtubedata(
-- 	title VARCHAR (100) NOT NULL,
-- 	date TIMESTAMP NOT NULL,
-- 	description TEXT NOT NULL,
-- 	thumbnail VARCHAR (50) NOT NULL,
-- 	url VARCHAR (50) NOT NULL
-- );
	
-- CREATE TABLE imdbdata(
-- 	title VARCHAR (100) NOT NULL,
-- 	date TEXT NOT NULL
-- );

SELECT * FROM public.youtubedata WHERE title = "Not Easy Being Green"
-- SELECT * FROM public.imdbdata
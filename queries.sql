-- DROP TABLE youtubedata;
-- DROP TABLE imdbdata;

-- CREATE TABLE youtubedata(
--  id SERIAL PRIMARY KEY,
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

SELECT * FROM dupe WHERE title = 'Mondays on CBS'
-- SELECT * FROM public.imdbdata

-- DELETE FROM youtubedata a USING youtubedata b
-- WHERE a.id > b.id
-- 	AND a.title = b.title;

DELETE FROM dupe
WHERE id IN
    (SELECT id
    FROM 
        (SELECT id,
         ROW_NUMBER() OVER( PARTITION BY title
        ORDER BY  id ) AS row_num
        FROM dupe ) t
        WHERE t.row_num > 1 );
		
create table dupe as (select * from youtubedata);
select * from dupe
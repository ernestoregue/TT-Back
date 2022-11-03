USE places;

create table place(
   place_id INT NOT NULL AUTO_INCREMENT,
   place_name VARCHAR(100) NOT NULL,
   place_hashtag VARCHAR(40) NOT NULL,
   place_city VARCHAR(40) NOT NULL,
   place_comment VARCHAR(120) NOT NULL,
   place_subjectivity FLOAT NOT NULL,
   place_polarity FLOAT NOT NULL,
   place_sentiment VARCHAR(10) NOT NULL,
   place_latitude VARCHAR(20) NOT NULL,
   place_longitude VARCHAR(20) NOT NULL,
   PRIMARY KEY ( place_id )
);

-- drop table place;
DROP TABLE place;

-- show info
SELECT * FROM place;

-- insert data to table place
INSERT INTO place (place_name, place_hashtag, place_city,place_comment, place_subjectivity, place_polarity, place_sentiment, place_latitude, place_longitude) 
values (
   'Tequisquiapan', 
   'tttequisquiapan', 
   'Tequisquiapan',
   'Me encanta muchisimo este lugar.', 
   0.5, 
   0.6, 
   'positive', 
   '-99.88828', 
   '20.52230'
   );
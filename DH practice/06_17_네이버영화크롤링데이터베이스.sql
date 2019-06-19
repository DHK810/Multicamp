-- 네이버 영화 데이터베이스
create database naver_movie;

use naver_movie;

CREATE TABLE `naver_movie`.`movie` (
  `code` INT NOT NULL,
  'title' varchar(255) NOT NULL,
  'story' TEXT(),
  'release_date' DATE,
  'created_date' DATETIME
  PRIMARY KEY (`code`));

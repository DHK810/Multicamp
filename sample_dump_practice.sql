select * 
from 상품 as p
inner join 메이커 as m
where p.메이커명 = m.메이커명;

select * 
from 상품2 as p
where p.메이커코드 = (
	select m.메이커코드
    from 메이커 as m
    where m.메이커코드 = 'M001'
    );

select * 
from sample25
where text like '%\%%';

SELECT *, price * quantity as total
FROM sample34
where price * quantity > 3000;

select *,
case a
	when 1 then '남자'
    when 2 then '여자'
    else 'n/a'
end as 성별
from sample37;

select *
from sample41;

-- insert
desc sample41;

insert into sample41 values(1, '헬로우', '2019-05-05');
insert into sample41(no, a)
values(2, '안녀엉');

insert into sample41(a, no)
values('블라브라',3);

insert into sample41(no, a, b)
values(4, NULL,  '2017-05-05');

-- use database
select *
from northwind1.categories;

show databases;
use northwind1;
use sample;

select *
from sample41;

delete
from sample41
where no = 4;

insert into sample41 values(4, '안녕', '2019/05/21');
insert into sample41 values(1, 'asdf', '2019/05/22');
desc sample41;

update sample41
set a = '즐거운 sql'
where no = 1;

update sample41
set a = NULL
where no = 2;

update sample41
set a = 'update', b='2019/06/14';

select count(name), count(quantity), count(*)
from sample51
where name = 'A';

select count(distinct name)
from sample51;

select sum(quantity)
from sample51;

select name, count(name), sum(quantity)
from sample51
group by name;

-- having

select name, count(name), sum(quantity)
from sample51
group by name
having sum(quantity) < 5;

select *
from sample54
where a = (
	select max(a)
	from sample54
    );

desc sample54;
update sample54
set a = 1
where a = (
	select max(a)
    from sample54
    );
    
select *
from (
	select *
    from sample54
) as a;

-- exists
select * 
from sample551;

select *
from sample552;

update sample551
set a = '있음'
where 
exists (
	select no2
    from sample552
    where no2 = no
    );
    
    
update sample551
set a = '없음'
where 
not exists (
	select no2
    from sample552
    where no2 = no
    );
    
select *
from sample551
where no in (
	select no2
    from sample552
    );
    
    select *
    from sample72_x, sample72_y;
    
-- join

select *
from `상품`;

select *
from `재고수`;

select *
from `상품`, `재고수`
where `상품`.상품코드 = `재고수`.상품코드;

-- 카티전
select *
from `상품`
inner join `재고수`
on `상품`.상품코드 = `재고수`.상품코드;

select *
from `상품`
left join `재고수`
on `상품`.상품코드 = `재고수`.상품코드;

create table books(
	book_id INT NOT NULL,
    title varchar(50),
    content text default '' NOT NULL,
    author_id INT,
    constraint pkey_sample
    primary key (book_id)
    );
alter table books add published_at DATETIME;
alter table books
modify title varchar(100);
alter table books
drop author_id;
    
desc books;

drop table books;	

CREATE index btree on books(title);

drop index btree on books;

select * from sample54;
create view sample_view67
as select * from sample54;

select * from sample_view67;

-- transaction
desc books;

start transaction;
insert into books values(1, '연금술사', '금 찾아 떠나자',
NULL);


insert into books values(2, '다크메이지', '어두운 메이지',
NULL);
insert into books values(3, '채식주의자', '베지테리언',
NULL);

commit;
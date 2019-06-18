select * from customers where not country = 'France' and not contactname LIKE 'Mar%';

DESC products;
select supplierid, unitprice from products where unitprice BETWEEN 15 and 20;


select * from customers where postalcode is not Null;
desc products;
select * from products order by unitsonorder ASC , unitprice DESC;

select * 
from customers 
where country = 'UK' 
order by contactname limit 3
offset 5;

select 
*,
case 
	when unitprice < 10 then '저'
    when unitprice > 50 then '중'
    else '고'
end as '가격'
from products;
-- 이름 바꾸기
select productid as 'ID' , productname as '이름', unitprice as '가격'
from products;

-- 집계 함수
select count(*)
from products;

select count(region)
from customers;

-- group by
select country, count(contactname)
from customers
group by country;

select country, city, count(contactname)
from customers
group by country, city;

-- Q. 국가별 고객수를 조회하고 그 중 5명 초과인 국가만 조회 (고객수 내림 차순): 국가명, 고객수
select country, count(contactname) as 'numOfCustomer'
from customers
group by country
having count(contactname) > 5;
-- having은 group by 된거 이후에 사용해야한다.

select country, count(contactname) as 'numOfCustomer'
from customers
-- where
group by country
having count(contactname) > 5
order by country desc;



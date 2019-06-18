select *
from products
where unitprice between 15 and 20;

-- Q. 가격이 15에서 20사이인 상품(Products) 의 생산자 목록 조회
select *
from suppliers
where SupplierID = (
	select supplierID
    from products
    where unitprice between 15 and 20
);

select supplierid,
case supplierid
	when 1 then 'a'
    when 2 then 'b'
    when 3 then 'c'
    else 'd'
end as '연습'
from products;

-- column 만들기
select unitprice, unitprice*2
from products;

-- alias
desc customers;
select customerid, city, address, country as C
from customers
group by country
order by count(*) desc;

-- alias
select customerid, city, address, country
from customers as C
where country = 'usa';

-- alias
select count(*)
from products, suppliers;

select products.productID, products.productName, products.supplierID, suppliers.companyName
from products, suppliers
where products.supplierID = suppliers.supplierID;


select p.*, s.*
from products as p, suppliers as s 
where p.supplierID = s.supplierID;
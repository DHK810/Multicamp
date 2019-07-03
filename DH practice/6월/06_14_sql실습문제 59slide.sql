-- Q. 런던에 위치한 공급자(Supplier)가 생산한 상품 목록 조회 : 도시명, 공급자명, 상품명, 상품가격

select s.city, s.companyname, p.productname, p.unitprice
from suppliers as s
inner join products as p
on s.city = 'London';

-- Q. 분류가 Seafood 인 상품 목록 (모든 컬럼 조회) : 분류, 상품 모든 컬럼

select categories.CategoryName, products.*
from products
inner join categories 
on categories.CategoryName = 'Seafood';

-- Q. 공급자(Supplier) 국가별, 카테고리 별 상품 건수, 평균가격 : 국가명, 카테고리명, 상품건수, 평균가격
select country, categoryName, UnitsOnOrder, 
from suppliers
join categories, products
order by UnitsOnOrder DESC;

-- Q. 상품 카테고리별, 국가별, 도시별 주문건수 2건 이상인 목록 : 카테고리명, 국가명, 도시명, 주문건수

-- select categoriesName, country, city, UnitsOnOrder
-- from 

-- Q. 주문자, 주문정보, 직원정보, 배송자정보 통합 조회 : 고객컬럼 전체, 주문정보 컬럼 전체, 배송자 정보 컬럼 전체 (4개 테이블 조인)

SELECT c.*, o.*, e.*, s.*
from orders as o
join customers c on c.customerID = o.customerID
join shippers s on s.shipperID = o.ShipVia
join employees e on o.EmployeeID = e.EmployeeID;


-- Q. 판매량(Quantity) 상위 TOP 3 공급자(supplier) 목록 : 공급자 명, 판매량, 판매금액
select s.ContactName, sum(od.quantity), (od.Unitprice * od.quantity) as sales
from orderdetails as od

join products p on od.productID = p.productID
join suppliers s on p.supplierID = s.supplierID
group by s.contactName
order by sales DESC
limit 3;

-- Q. 상품(Product) 분류(Category)별, 고객 지역별(City) 총 판매량 기준으로 정렬하여 
-- : 카테고리명(categoryName), 고객지역명(City),  총 판매량
SELECT cg.categoryName, c.City, totalsales
from products as p
join categories c on p.categoryID = c.categoryID
join orderdetails od on;

-- Q. 고객 국가가 USA이고, 상품별 판매량(Quantity 수량 합계) 순위(정렬하여) : 
-- 국가명(Country), 상품명(ProductName), 판매량, 판매금액

SELECT c.country, p.productNAme, count(od.quantity), (od.unitprice * od.quantity) as totalsales
from orderdetails as od

join products p on p.productID = od.productID
join orders o on o.orderID = od.orderID
join customers c
where c.country = 'USA'
group by p.ProductName
-- order by (od.unitprice * od.quantity) DESC;
select customerID, contactName, EmployeeID, LastName, Title, c.city
from customers as c
inner join employees as e
on c.city = e.city;

-- join
select productID, productNAme, p.supplierID, s.companyName
from products as p
join suppliers as s 
on p.supplierID = s.supplierID
order by s.supplierID
limit 10;

-- outer join
select productID, productNAme, p.supplierID, s.companyName
from products as p
left outer join suppliers as s 
on p.supplierID = s.supplierID
order by s.supplierID
limit 10;

select productID, productNAme, p.supplierID, s.companyName
from products as p
right outer join suppliers as s 
on p.supplierID = s.supplierID
order by s.supplierID
limit 10;
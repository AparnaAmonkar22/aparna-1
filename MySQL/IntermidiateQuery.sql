use Northwind;

select * from customers where not country='Germany';

select * from customers where country='Germany' and (city='berlin' or city='stuttgart');

select * from customers where not country = 'germany' and not country = 'usa';

select * from customers order by country; -- asce by default

select * from customers order by country desc;

select * from customers order by customername, country;

select * from dept;

insert into dept (id,dpt_name) values (4, 'Management');

select * from customers where address is not null;

select * from customers where address is null;

update dept set dpt_name='Library' where id=4;

-- Disable safe mode off to query without primary key	
 SET SQL_SAFE_UPDATES = 0;

update customers set postalcode=00000 where country='mexico';

select * from customers where country = 'mexico';

select * from customers where customername like 'a%';  -- CustomerName starts with 'a'
select * from customers where customername like '%e'; -- CustomerName ends with 'e'
select * from customers where customername like '%world%'; -- CustomerName contains 'world'

select * from customers where country in ('Germany', 'France');
select * from customers where country not in ('germany','france','uk');

select * from products where price not between 10 and 20;

select * from products where price between 10 and 20 and categoryid not in (1,2,3);

select productID AS ID, productName AS Product from Products;

-- INNER JOIN
select orders.orderId, customers.customerName, orders.orderDate from orders INNER JOIN customers ON orders.customerId=customers.customerId;

-- LEFT JOIN
select orders.orderId, customers.customerName from customers LEFT JOIN orders ON customers.customerId=orders.customerId order by customerName;

-- RIGHT JOIN
select orders.orderId, Employees.FirstName, Employees.LastName from orders RIGHT JOIN employees ON orders.employeeId=employees.employeeId where orders.orderId IS NOT NULL order by orderId;

-- CROSS JOIN
select customers.customerId, customers.customerName, orders.orderId from customers CROSS JOIN orders;

-- SELF JOIN -- 
select A.customerName AS CustomerName1, B.customerName AS CustomerName2, A.City from customers A, Customers B where A.customerId <> B.customerId AND A.city=B.city Order By A.city;

-- UNION -- removes duplicate
select City from customers UNION select City from suppliers order by City;
select City,Country from customers where country='germany' UNION select City,Country from suppliers where country='france';


-- UNION ALL
select City from customers UNION ALL select City from suppliers;
select City,Country from customers where country='germany' UNION ALL select City,Country from suppliers where country='france';





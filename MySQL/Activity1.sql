use testschema;

show tables;

-- 1. Write a query to display all the agents name with their phone number from agents table.
select agent_name,phone_number from agents;

-- 2. Write a query to display the names of all the customers with working area is Leeds from customer table.
select cust_name as Name from customer where working_area='Leeds';

-- 3. Write a query to display the order number and order amount with order description is shoes from orders table.
select order_num, order_amount from orders where order_description='shoe';

-- 4. Write a query to display the agent code, order amount and order description where order amount= 3000 and order description is clothes
select agent_code, order_amount, order_description from orders where order_amount=3000 and order_description='clothes';

-- 5. Write a query to display all the details from the table order where the order amount is more than 2000.
select * from orders where order_amount>2000;

-- 6. Write a query to display customer name and customer phone number that have alphabet ‘e’ in their name.
select cust_name, phone_number from customer where cust_name like '%o%';

-- 7. Write a query to display all the details from orders table with minimum order amount.
select * from orders where order_amount = (select min(order_amount) from orders); 

-- 8. Write a query to display the total order amount from orders table.
select sum(order_amount) from orders;

-- 9. Write a query to find the number of agents currently listing for all of their customers from orders table.
select count(distinct agent_code) from orders;

-- 10 Write a query to find the highest purchase amount ordered by the each customer code and highest order amount. --
select cust_code, max(order_amount) from orders group by cust_code;

-- 11. Write a query to find the highest order amount on a date '2022-07-13' with agent code.
select agent_code, max(order_amount) from orders where order_date='2022-07-13' group by agent_code;

-- 12. Write a query to find the name and customer city of those customers and agents who work in the same city.
select cust_name, agent_name, cust_city from customer,agents where customer.working_area=agents.working_area;

-- 13. Write a query to find the name of all the customer names along with the agent names who works for them.
select cust_name, agent_name from customer, agents where agents.agent_code=customer.agent_code order by customer.cust_code;

-- 14. Write a query to display all those orders by the customers not located in the same cities where their agents working area.
select * from customer where customer.working_area not in (select working_area from agents);

-- 15. Write a query to display all the orders issued by the agent 'Melvin' from the orders table.
select * from orders where agent_code=(select agent_code from agents where agent_name='Melvin');



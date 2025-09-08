create database car_db;

use car_db;

show tables;

-- 1. Read Cars Data
select * from car_data;

-- 2. Total Cars: To get a count of total records.
select count(*) as Total_Cars from car_data;

-- 3. The Client asked me to show, how many cars will be available in 2023?
select count(*) as Total_Cars from car_data where year='2023';

-- 4. The Client asked me to show, how many cars is available in 2020,2021,2022?
select count(*) as Total_Cars from car_data where year IN ('2020','2021','2022');

-- 5. Client asked me to print the totals of all cars by year. I don’t see all the details.
select Year, count(*) as Total_Cars from car_data group by year;

-- 6. Client asked to car dealer agent, how many diesel cars will there be in 2020?
select count(*) as Total_Cars from car_data where year=2020 and fuel='diesel';

-- 7. How many petrol cars will be there in 2020?
select count(*) as Total_Cars from car_data where fuel='petrol' and year='2020';

-- 8. Give a print of all the fuels cars (petrol, diesel, and CNG) come by all years?
select Year, Name, Fuel from car_data order by year;

-- 9. Were more than 100 cars in a given year, which year had more than 100 cars?
select Year, count(*) AS Total_Cars from car_data group by year having count(*)>100; 

-- 10. Count All cars details between 2019 and 2022 need a complete list?
select  count(*) as Total_Cars_In_2019To2022 from car_data  where year  between '2019' and '2022';

-- 11. All cars details between 2019 to 2022, need complete list?
select *  from car_data where year between '2019' and '2022';


show databases;
use sqltut;
show tables;
create table employees (Emp_Id int primary key, Emp_name varchar(25), Age int, Gender char(1), Doj date, Dept varchar(20), City varchar(15), Salary float);
insert into employees values 
(1, 'Jhon', 23, 'M', '2019-05-01', 'Sales', 'Vegas',30000.00),
(2, 'Maze', 22, 'F', '2019-06-07', 'Marketing', 'Sydney',60000.00),
(3, 'Chloe', 24, 'F', '2019-07-11', 'Sales', 'Amsterdam',50000.00),
(4, 'Adam', 28, 'M', '2020-01-01', 'Development', 'DownHill',35000.00),
(5, 'Evan', 31, 'M', '2020-09-13', 'Marketing', 'Vegas',38000.00),
(6, 'Amini', 20, 'F', '2021-08-09', 'Sales', 'Vegas',40000.00);
select * from employees;
select distinct dept from employees;
select avg(age) as avg_age from employees;
 
# Avg age in each department
select dept, round(avg(age),0) as avg_age from employees group by dept;
select city, sum(salary) as total_salary from employees group by city;
select count(emp_id), city from employees 
group by city 
order by count(emp_id) desc;

select year(doj) as year, count(emp_id) as num_emp from employees
group by year(doj);


# Using group by to join two or more table
create table sales (product_id int, sell_price float, quantity int, state varchar(20));
insert into sales values
(1,23.5,3,'Punjab'),
(2,55.0, 1, 'UP'),
(3,65.0,2, 'Goa'),
(4,100.0, 10, 'Haryana'),
(5,45.0,1,'Bihar');
select * from sales;

select product_id, sum(sell_price * quantity) as revenue from sales group by product_id;

create table cp_product(product_id int, cost_price float);
insert into cp_product values
(1,20),
(2,50),
(3,60),
(4,90),
(5,41);

select c.product_id, sum(s.sell_price - c.cost_price) * s.quantity as profit from sales as s inner join cp_product as c where s.product_id = c.product_id
group by c.product_id;


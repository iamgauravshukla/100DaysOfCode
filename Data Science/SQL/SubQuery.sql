show databases;
use sqltut;
show tables;

# Subqueries using Select
select emp_name, dept, salary from employees
where salary < (select avg(salary) from employees);

# Subqueries using INSERT
create table products
(product_id int, item varchar(30), sell_price float, product_type varchar(20));

insert into products 
values(101, 'LG Wing', 65000, 'Mobile'),
(102, 'Iphone 12', 56000, 'Mobile'),
(103, 'Macbook Air', 102000, 'Laptop'),
(104, 'Mi Notebook', 55000, 'Laptop');


create table orders
(order_id int, product_sold varchar(20), selling_price float);

insert into orders
select product_id, item, sell_price from products 
where
product_id in (select product_id from products where sell_price > 60000);

select * from orders;


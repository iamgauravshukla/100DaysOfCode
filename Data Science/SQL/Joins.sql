 create database sql_joins;
 show databases;
 use sql_joins;
 
create table cricket (cricket_id int auto_increment, name varchar(20), primary key(cricket_id));
create table hockey (hockey_id int auto_increment, name varchar(20), primary key(hockey_id));

insert into cricket (name)
values ('Gaurav'), ('Arun'), ('Munna'), ('Guddu'), ('Bassi');
 
insert into hockey (name)
values ('Gaurav'), ('Arun'), ('Samule'), ('Sunnuy'), ('Albert');

# To find the students that are part of both sports we use Inner Join
select * from cricket as c inner join hockey as h on c.name = h.name;

# selecting individual 
select c.cricket_id, c.name, h.hockey_id, h.name 
from cricket as c inner join hockey as h on c.name = h.name;

#Another example on different database
use classicmodels;
show tables;

select * from products;
select * from productlines;
select * from orders;
select * from orderdetails;

# Example 1  
select productcode, productname, textdescription
from products
inner join productlines
using (productline);

# Example 2
select o.ordernumber, o.status, p.productname,
sum(quantityordered * priceeach) as revenue
from orders as o
inner join orderdetails as od on o.ordernumber = od.ordernumber 
inner join products as p on p.productcode = od.productcode
group by ordernumber;

# Left Join 
select * from customers;
select * from orders;

select c.customernumber, c.customername, ordernumber, status
from customers as c left join orders as o
on c.customernumber = o.customernumber
where ordernumber is null;
# to check null values


# Right Join
select * from customers;
select * from employees;

select c.customername, c.phone, e.employeenumber, e.email 
from customers as c right join employees as e
on e.employeenumber = c.salesrepemployeenumber
order by employeenumber;

#self join
select concat(m.firstname, ' ', m.lastname ) as manager,
concat(e.firstname, ' ', e.lastname) as employee
from employees as e
inner join employees as m on 
m.employeenumber = e.reportsto
order by manager;

# Full Join
#This method is only for MySql Workbench

select c.customername, o.ordernumber
from customers as c left join orders as o
on c.customernumber = o.customernumber
union
select c.customername, o.ordernumber
from customers as c right join orders as o
on c.customernumber = o.customernumber;



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


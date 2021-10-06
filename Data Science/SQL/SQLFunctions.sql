use sqltut;
select count(Age) as emp_age from emp_details;
select sum(salary) from emp_details;
select avg(salary) from emp_details;
-- Selecting specific columns 
select name, age from emp_details;
-- Conditional selection using where
select name from emp_details where salary > 40000; 
select * from emp_details where sex = "F";
-- Operators
-- 1: OR
select * from emp_details where city = 'Delhi' or city = 'Pune';
-- 2: IN
select * from emp_details where city in ('Agra', 'Pune');
-- Date filter

select * from emp_details where doj between '2000-01-01' and '2022-12-01';
select * from emp_details;


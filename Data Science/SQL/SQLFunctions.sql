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

select * from emp_details where doj between '2020-01-01' and '2020-12-01';
select * from emp_details where age > 20 and sex = 'M';

-- Group By
select sex, sum(salary) as total_salary from emp_details group by sex;

-- Sorting the order in ascending 
select * from emp_details order by salary;
 -- Sorting the order in dscending 
select * from emp_details order by salary desc;
 
 -- Some basic operations
select (20-35) as subtract;
select length('Argentina') as stringLen;
select repeat('@', 10);
select upper('Gaurav');
select lower('SANIDHYA');
select current_date();
select day(current_date());
select now();

# String Functions\
select upper('Gaurav') as upperCase;
select lower('MONITOR') as lowerCase; # lcase can also be used here

select name, character_length(name) as total_len from emp_details;
-- or
select name, char_length(name) as total_len from emp_details;

select concat('Do', ' you', ' now me ?') as concated;

select name, sex, concat(name, ' sex is ', sex) as gender from emp_details;

select reverse('Happy Birthday') as revStr;

select name , replace(name, 'Gulshan Anand', 'Saurav Shukla') as replaced from emp_details;

-- Trim Functions
select ltrim('     Hey There!') as leftTrimmed;
select rtrim('Whats Up..      ') as rightTrimmed;
select trim('    Hello     ') as bothTrimmed;

-- Position Function
select position('banana' in 'banana is a fruit') as namePos;

-- ASCII
select ascii('a');
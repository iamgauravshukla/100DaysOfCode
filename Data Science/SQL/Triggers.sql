create database triggers;
use triggers;

# Before insert trigger
create table customers 
(customer_id int, age int, name varchar(20));

delimiter //
create trigger age_verify
before insert on customers
for each row
if new.age < 0 then set new.age = 0;
end if;
//

insert into customers values
(101, 20, 'Pawan Kalyan'),
(102,  -5, 'Ravi Teza'),
(103, 21, 'Prabhas'),
(104, -23, 'Mahesh Babu');

select * from customers;

# After Insert Trigger

create table customers_a
(id int auto_increment primary key, name varchar(20) not null, email varchar(30), birthdate date);

create table message
(id int auto_increment, message_id int, message varchar(100) not null, primary key(id, message_id));

delimiter //
create trigger check_birtdate
after insert
on customers_a
for each row
begin
if new.birthdate is null then
insert into message( message_id, message)
values (new.id, concat('Hey', new.name, 'Please update your date of birth'));
end if;
end //

insert into customers_a(name, email, birthdate)
values ('Gaurav', 'gaurav@gmail.com', null),
('Sanidhya', 'sanidhya@abc.com', '1998-12-22'),
('Krish', 'krish@xyz.com', '1997-08-20'),
('Saurav', 'saurav@gmail.com', null);

select * from message;

# Beofre Update 
create table employees
(emp_id int primary key, emp_name varchar(20), age int, salary float);

insert into employees values
(101, 'Jimmy', 35, 70000),
(102, 'Shane', 30, 55000),
(103, 'Marry', 28, 62000),
(104, 'Dwayne', 37, 57000),
(105, 'Ammy',35, 80000);

delimiter //
create trigger upd_trigger
before update 
on employees
for each row
begin 
if new.salary = 10000 then 
set new.salary = 85000;
elseif new.salary < 10000 then
set new.salary = 72000;
end if;
end //

update employees
set salary = 8000;

select * from employees;

# Before delete trigger

create table salary
(eid int primary key, validfrom date not null, amount float not null);

insert into salary(eid, validfrom, amount) values
(101,'2005-06-14',80000),
(102, '2006-08-11', 68000),
(103, '2007-09-12', 72000);

create table salarydel (id int primary key auto_increment, eid int, validfrom date not null, amount float not null, deletedat timestamp default now());

delimiter $$
create trigger salary_del
before delete
on salary
for each row
begin
insert into salarydel(eid, validfrom, amount)
value(old.eid, old.validfrom, old.amount);
end $$

delete from salary
where eid = 103;

select * from salarydel;


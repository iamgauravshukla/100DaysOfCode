use sqltut;

select count(emp_id), city from employees group by city
having count(emp_id) > 0;

select dept, avg(salary) as avg_salary from employees group by dept
having avg(salary) > 40000; 

select city, sum(salary) as total from employees group by city
having sum(salary) > 15000;

select dept, count(*) as emp_count from employees group by dept
having count(*)>1;

# Where with having

select city, count(*) as emp_count from employees
where city != 'DownHill'
group by city
having count(*)>0;
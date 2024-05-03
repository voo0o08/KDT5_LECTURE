use sqlclass_db;

# 테이블 생성
create table customer
	(customer_id smallint unsigned,
	first_name varchar(20),
	last_name varchar(20),
	birth_date date,
	spouse_id smallint unsigned,
	constraint primary key (customer_id)
	);
	
desc customer;      

insert into customer
values
 (1,	'John',	'Mayer',	'1983-05-12',	2),
 (2,	'Mary',	'Mayer',	'1990-07-30',	1),
 (3,	'Lisa',	'Ross',	'1989-04-15',	5),
 (4,	'Anna',	'Timothy',	'1988-12-26',	6),
 (5,	'Tim',	'Ross',	'1957-08-15',	3),
 (6,	'Steve',	'Donell',	'1967-07-09',	4);
 
insert into customer	(customer_id, first_name, last_name, birth_date)
values(7, 'Donna', 'Trapp',	'1978-06-23');

select  cust.customer_id,
 cust.first_name,
 cust.last_name,
 cust.birth_date,
 cust.spouse_id,
 spouse.first_name as spouse_firstname,
 spouse.last_name as spouse_lastname
 
from customer as cust
	inner join customer as spouse
	on cust.spouse_id = spouse.customer_id;

/*
 * JOHN이라는 이름의 배우가 출연한 모든 영화의 제목 출력 
 */
use sakila;

select title
from film as f
	inner join film_actor as fa on f.film_id = fa.film_id
	inner join actor a on fa.actor_id = a.actor_id 
where a.first_name = "JOHN";

/*
같은 도시에 있는 모든 주소를 반환하는 쿼리 작성
address	테이블을 self-join,	각 행에는 서로 다른 주소가 포함
*/
select a1.address	as addr1,	a2.address	as addr2,	a1.city_id,	a1.district
 from address	as a1
 inner join address	as a2
 where (a1.city_id	=	a2.city_id)
 and (a1.address_id	!=	a2.address_id);
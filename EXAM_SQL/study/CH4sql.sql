select *
from customer
where not (first_name = "steven" or last_name = "young")
	and create_date > "2006-01-01";
# 2006-01-01 이후 태어난 사람 중 steven도 young도 아닌 사람을 찾음 

select *
from customer
where (first_name <> "steven" and last_name <> "young")
	and create_date > "2006-01-01";
	
select c.email
from customer c 
	inner join rental r
	on c.customer_id = r.customer_id 
where date(r.rental_date) = "2005-06-14";


select customer_id, rental_date
from rental
where rental_date <= "2005-06-16"
	and rental_date >= "2005-06-14";

select customer_id, rental_date
from rental
where rental_date between "2005-06-14"
	and "2005-06-16";

select customer_id, payment_date, amount
from payment; 

select last_name, first_name
from customer 
where last_name between "FA" and "FRZ";

select title, rating
from film
where rating in ("G", "PG");

select title, rating
from film
where rating in (select rating from film where title like "%PET%");

select title, rating 
from film 
where title like "%PET%";

select last_name, first_name
from customer
where left(last_name, 2) = "QU";

select last_name, first_name
from customer 
where last_name like "Q%" or last_name like "Y%";

select last_name, first_name
from customer 
where last_name regexp "^[QY]";

select rental_id, customer_id
from rental
where return_date is null;           

# 학습 점검 3.
select *
from payment
where amount in (1.98, 7.98, 9.98)

# 학습 점검 4. 성의 두 번째 위치에 A가 있고 다음에 W가 있는 모든 고객을 찾는 쿼리
select * from customer
where last_name like "_AW%"
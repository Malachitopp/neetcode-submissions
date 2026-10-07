-- Write your query below
select s.seller_name
from seller s
left join orders o on o.seller_id = s.seller_id
                  and o.sale_date >= '2020-01-01' and o.sale_date <= '2020-12-31'
where o.order_id is null
order by s.seller_name asc;
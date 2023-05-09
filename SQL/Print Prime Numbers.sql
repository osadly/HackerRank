with x as
(
select level+1 num from dual connect by level<1000
)
select listagg(x.num,'&') within group (order by num) from x 
where not exists
(
    select 1 from x x2
    where x.num > x2.num and remainder(x.num,x2.num)=0
)


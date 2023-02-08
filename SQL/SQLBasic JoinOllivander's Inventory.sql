/* id, age, coins_needed, and power */
with tmp_tbl as 
(
    select wp.age, min(wd.coins_needed) min_coins_needed,wd.power
    from wands wd,wands_property wp
    where 1=1
    and wd.code=wp.code
    and wp.is_evil=0
    group by wp.age , wd.power
    having min(wd.coins_needed) >=0 
)
select wd.id,wp.age, wd.coins_needed,wd.power
from tmp_tbl, wands wd,wands_property wp
where 1=1
and wd.code=wp.code
and wp.age=tmp_tbl.age
and wd.coins_needed=tmp_tbl.min_coins_needed
and wd.power=tmp_tbl.power
order by wd.power desc, wp.age desc;
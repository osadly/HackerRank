select * from projects;
--========================================================================================================
select count (*) from projects;
--========================================================================================================
select 'q1' , p11.task_id,p21.task_id, p11.start_date sd1, p11.end_date
from projects p11, projects p21
where
1=1
--and p11.task_id <> p21.task_id 
and p21.start_date = p11.start_date
and p11.task_id not in
(
    select p11_task_id from (
        select p12.task_id p11_task_id,p22.task_id, p12.start_date sd1, p12.end_date
        from projects p12, projects p22
        where
        1=1
        --and p12.task_id <> p22.task_id 
        and p22.start_date = p12.end_date
        )
)
union all
(
    select 'q2' , p12.task_id p11_task_id,p22.task_id, p12.start_date sd1, p12.end_date
        from projects p12, projects p22
        where
        1=1
        --and p12.task_id <> p22.task_id 
        and p22.start_date = p12.end_date
);
--========================================================================================================
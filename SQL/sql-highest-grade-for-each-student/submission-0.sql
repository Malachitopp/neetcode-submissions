-- Write your query below
select student_id, exam_id, score 
FROM (select student_id, exam_id, score,
ROW_NUMBER() OVER (PARTITION by student_id ORDER BY score desc, exam_id asc) as rn 
FROM exam_results) ranked 
where rn = 1 
order by student_id
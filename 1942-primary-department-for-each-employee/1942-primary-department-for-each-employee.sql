# Write your MySQL query statement below

WITH choose AS (
SELECT 
employee_id, 
department_id, 
ROW_NUMBER ( ) OVER ( PARTITION BY employee_id ORDER BY primary_flag ASC) AS rn
FROM Employee e 
)

SELECT 
employee_id, department_id 
FROM choose 
WHERE rn = 1

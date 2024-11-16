# Write your MySQL query statement below
WITH SecondSalary 
AS (
    SELECT DISTINCT salary as "SecondHighestSalary"
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1
    OFFSET 1
)

SELECT (SELECT * FROM SecondSalary) AS "SecondHighestSalary"
FROM DUAL;
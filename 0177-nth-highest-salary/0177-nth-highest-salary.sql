CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE OffsetValue INT;
    SET OffsetValue = N - 1;
    RETURN (
        SELECT IFNULL ((
                SELECT DISTINCT salary
                FROM Employee
                ORDER BY salary DESC
                LIMIT 1
                OFFSET OffsetValue
        ), NULL)
    );
END
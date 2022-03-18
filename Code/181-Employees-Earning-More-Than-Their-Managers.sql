# Advantage of a JOIN
# Execution and retrieval time faster than subqueries.

# Disadvantages Of JOIN:
# Database server has to do more work when it comes to a lot of joins in a query => more time consuming to retrieve data
# Developer can be confused to choose the appropriate type among many types of joins.

# Write your MySQL query statement below
SELECT
     a.NAME AS Employee
FROM Employee AS a JOIN Employee AS b
     ON a.ManagerId = b.Id
     AND a.Salary > b.Salary
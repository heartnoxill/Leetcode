# Write your MySQL query statement below
# Using Transact SQL is the easiest way
Select Score,
       Dense_rank() Over (Order By Score Desc) `Rank`
From Scores
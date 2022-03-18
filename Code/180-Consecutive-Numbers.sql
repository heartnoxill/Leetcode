# Write your MySQL query statement below

# if the table is
# 1 , 1
# 2 , 1
# 3 , 1
# 4 , 1
# 5, 25

# first
# 1 , 1 = 1 , 1
# 1+1 , 1 = 2, 1
# 1+2 , 1 = 3, 1
# and returns true

# then
# 2 , 1 = 2, 1
# 2+1 , 1 = 3, 1
# 2+2 , 1 = 4, 1
# and returns true

# then
# 3 , 1 = 3, 1
# 3+1 , 1 = 4, 1
# 3+2 , 1 = 5, 25
# and returns false

select distinct Num as ConsecutiveNums
from Logs
where (Id + 1, Num) in (select * from Logs) and (Id + 2, Num) in (select * from Logs)
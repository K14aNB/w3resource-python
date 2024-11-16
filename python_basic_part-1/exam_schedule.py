"""
Task
----
Write a python program to display the examination schedule. (extract the date from exam_st_date).

Sample Input:
exam_st_date = (11, 12, 2024)

Output:
The examination will start from : 11 / 12 / 2024
"""

# Month, Date, Year as input
exam_st_date_mdy = tuple(input().split(","))

print(
    f"The examination will start from (mm / dd / yyyy) : {exam_st_date_mdy[0]} / {
        exam_st_date_mdy[1]} / {exam_st_date_mdy[2]}"
)

print(
    f"The examination will start from (dd / mm / yyyy) : {exam_st_date_mdy[1]} / {
        exam_st_date_mdy[0]} / {exam_st_date_mdy[2]}"
)

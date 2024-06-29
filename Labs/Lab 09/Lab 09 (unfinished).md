# Lab 09: Number of Days Design

## Step 1: By Hand
Compute the number of days between the following dates:
 - 15th of October, 1999 and 25th of October, 1999
 - 23rd of October, 1999 and 1st of December, 1999
 - 21st of October, 1999 and the 4th of March, 2004

## Step 2: Approach
First, figure out if it's a leap year, for each year, and if so account for that in the number of days in the year, or within the year the number of days in February. Then, figure out how many full years between each day and calculate the number of days that is. Then, figure out how many full months between each day and figure out how many days that is. Finally, figure out how many remaining days are between the two days and add up the total number of days.

## Step 3: Pseudocode
```
day_1 = INPUT
month_1 = INPUT
year_1 = INPUT
day_2 = INPUT
month_2 = INPUT
year_2 = INPUT

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

years_between = year_2 - year_1
months_between = 0
number_of_leapyears = 0
days_between = 0


```
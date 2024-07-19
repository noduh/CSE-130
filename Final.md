# Final Exam: Find The Missing Number
The problem definition is as follows, quoted from the final exam instructions.
 > You are given an array of size n with the range of numbers from 1 to n+1. This array has no duplicates, one number is missing, and the array is not sorted. Find the missing number.

## Finding The Solution 
I originally had thought of a very efficient solution, but it unfortunately required the list to be sorted. Because of this, I thought it might be good to try sorting the list. I eventually got this down to a fairly efficient sort and was about to use that solution. However, I overheard (not sure if it's in the context of the final or not) someone mentioning subtraction.

Having heard this, I realized I can find the missing number by subtracting the sum of all the numbers from the sum of all numbers from `1` to `n + 1`. In addition to this, I remembered that in another class I had the task of writing a proof about the sum of all numbers from `1` to `n`. This led to me playing with numbers and eventually finding the equation `(n / 2) * (n + 1)`, which conveniently has an algorithmic efficiency of `O(1)`. All that's left is to add all the numbers in the list which has an efficiency of `O(n)` and subtract which has the efficiency of `O(1)`.

**This means that the program should have an overall algorithmic efficiency of `O(n)`.**

## Pseudocode
Using the algorithm I described as my solution above, I wrote the following pseudocode.

```
list = INPUT
n = LENGTH_OF(list) + 1
expected_sum = (n / 2) * (n + 1)
actual_sum = 0

FOREACH num IN list
    actual_sum += num

missing_number = expected_sum - actual_sum

RETURN missing_number
```

This program works with any length of list. (This includes a length of zero!) It's hard to assert efficiently in the program, but this works only with the list described in the problem definition. I will also describe below when finding the efficiency how to do this without a `LENGTH_OF()` function for finding the length of the list.

## Efficiency
As you can see, every line in the pseudocode has an efficiency of `O(1)`, with the exception of the loop which has an efficiency of `O(n)`. This means that **the overall efficiency is `O(n)`**. If the `LENGTH_OF()` function for some reason doesn't exist, you can simply add a counter to the loop and add one before calculating `expected_sum`. This won't change the algorithmic efficiency at all.
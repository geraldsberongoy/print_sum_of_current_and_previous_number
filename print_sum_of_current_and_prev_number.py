# Exercise 2: Print the sum of the current number and the previous number.

# Write a program to iterate the first 10 numbers, and in each iteration, 
# print the sum of the current and previous number.

# strategy
#   0, current=0, prev=0, so i + prev 0, using pre-assign variable prev=0 to make it right
#       then update current num to prev num
#   1, current=1, updated prev=0, sum=1, update prev 
#   2, current=2, updated prev=1, sum=3, update prev 
#   3, current=3, updated prev=2, sum=5, update prev 
#   4, current=4, updated prev=3, sum=7, update prev 
#   5, current=5, updated prev=4, sum=9, update prev 
#   6, current=6, updated prev=5, sum=11, update prev 
#   7, current=7, updated prev=6, sum=13, update prev 
#   8, current=8, updated prev=7, sum=15, update prev 
#   9, current=9, updated prev=8, sum=17, update prev

# pseudocode
# assign prev_num to 0
# for loop(10), first 10 numbers
#   print(current which is i, previous num, sum)
#   update the previous number

previous_num = 0
for current in range(10):
    print(f"Current number: {current}. Previous number: {previous_num}. Sum: {current + previous_num}")
    previous_num = current
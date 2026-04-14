"""
Write a python script to prompt users to enter the first and last values and generate some randome values between the two entered values.
"""

import random

start = int(input("Enter the minimum value : "))
end = int(input("Enter the maximum value : "))
count = int(input("How many values want to generate : "))

for i in range(count):
    val = random.randint(start,end)
    print(val)

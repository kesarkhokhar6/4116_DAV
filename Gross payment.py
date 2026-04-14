"""Write a program to prompt users to enter their working hours and rate per hour to calculate gross pay.
The program should give the employee 1.5 times the hours worked above 30 hours.
"""

h = float(input("Enter working hour : "))
r = float(input("Enter rate per hour : "))

if h>30:
    final = (30*r)+((h-30)*r*1.5)

else:
    final = h*r

print("Final payment is : ",final)

#Write a program for swapping of values of variables.

num1 = int(input("Enter number1 : "))
num2 = int(input("Enter number2 : "))

print(f"Before swapping num1 : {num1}, num2 : {num2}")
temp = num1
num1 = num2
num2 = temp
print(f"After swapping num1 : {num1}, num2 : {num2}")

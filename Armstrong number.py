#Write a program to check given number is armstrong number.

num = int(input("Enter number : "))
n = num
power = len(str(num))
total = 0

while n>0:
    digit = n % 10
    total += digit ** power
    n //= 10

if total == num:
    print(f"{num} is armstrong number.")
else:
    print(f"{num} is not armstrong number.")

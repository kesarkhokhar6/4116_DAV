#Find max values among two input values

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

if a>b:
    print(f"{a} is greater than {b}")
elif a==b:
    print(f"{a} and {b} are equal")
else:
    print(f"{b} is greater than {a}")

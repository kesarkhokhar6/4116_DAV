#Positive, Negative, Zero

try:
    n = int(input("Enter a number : "))

    if n>0:
        print(f"{n} is Positive")

    elif n==0:
        print(f"{n} is Zero")

    else:
        print(f"{n} is Negative")

except ValueError:
    print("Wrong input")

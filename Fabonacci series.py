#Write a program to create fabonacci series upto entered term.

a = 0
b = 1
n = int(input("Enter no. of terms : "))
print(a,b,sep="\n")

for i in range(3,n+1):
    c = a + b
    a = b
    b = c
    print(c)

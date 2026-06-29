# Take three numbers and print the largest.

a = int(input())
b = int(input())
c = int(input())
print(a if a>b and a>c else b if b>c else c)
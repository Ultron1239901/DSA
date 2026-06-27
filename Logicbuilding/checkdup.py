# Take a 3-digit number and check if all digits are distinct. 

# n = int(input())
# a = list(str(n))
# if len(a)==len(set(a)):
#     print("Distinct elements")
# else:
#     print("No distinct elements")

n = int(input("Enter a number"))
a = n%10
n = n // 10
b = n%10
n = n // 10
c = n%10
n = n // 10

if a!=b and b!=c and a!=c:
    print("Distinct elements")
else:
    print("Not distinct elements")
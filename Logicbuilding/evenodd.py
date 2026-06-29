# Take two numbers and determine whether both are even, both are odd, or one is 
# even and one is odd.
a ,b = map(int,input().split())
if a%2==0 and b%2 ==0:
    print("Both are even")
else:
    if a%2!=0 and b%2!=0:
        print("Both are odd")
    elif a%2==0:
        print("a is even")
    elif b%2==0:
        print("b is even")
    else:
        print("Enter a valid number")


#we can use the & bitwise operator to check the even or odd
# because the number is even the lsb is 0 and & operation with it result in 0
# in odd the & operation with it will not result in 0 but result in one in the lsb

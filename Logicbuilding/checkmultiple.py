a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
large = max(a,b)
small = min(a,b)

# if (a!=0 and a%b==0) or (b!=0 and b%a==0):
#     print("The number is multiple of one another")
# else:
#     print("The number is not the multiple of one another") 

# division better handle 0 edge case

#we can make division operation and check the answer is integer this can avoid the zero 

# we know the large number can divide the small number

if small!=0 and large%small==0:
    print("Multiple")
else:
    print("Not multiple")
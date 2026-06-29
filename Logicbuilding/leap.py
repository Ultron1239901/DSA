y = int(input("Enter the year: "))

if y%400==0:
    print("leap year")
elif y%4==0 and y%100!=0:
    print("Leap year")
else:
    print("Not a leap year")




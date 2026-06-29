# Take a month number (1–12) and print the number of days in that month (ignore leap 
# years). 

months ={
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

month = int(input("Enter the month: "))
if month in months:
    print(f"There are {months.get(month,0)} days in the {month}th month")
else:
    print("Enter a valid month")
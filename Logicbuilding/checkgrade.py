# Take marks (0–100) and print the corresponding grade (A/B/C/D/F)

marks = int(input("Enter the grade: "))
if marks<0 or marks>100:
    print("Enter a valid marks")
elif marks<=35:
    print("F grade")
elif marks<=50:
    print("D grade")
elif marks<=60:
    print("C grade")
elif marks<=80:
    print("B grade")
else:
    print("A grade")
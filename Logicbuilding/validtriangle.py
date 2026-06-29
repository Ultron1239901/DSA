class validTriangle:
    def validtri(self,a,b,c):
        if a+b>c and b+c>a and a+c>b:
            if a==b==c:
                print("Equilateral triangle")
            elif a==b!=c or a==c!=b or b==c!=a:
                print("Isoceles triangle")
            else:
                print("Scalene triangle")
        else:
            print("Not valid triangle")
vt = validTriangle()
a,b,c = map(int,input().split())
vt.validtri(a,b,c)
# print(vt.validtri(int(input("1st side")), int(input("2nd side")), int(input("3rd side"))))
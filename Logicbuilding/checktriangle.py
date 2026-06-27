class validTriangle:
    def validtri(self,a,b,c):
        return "Valid triangle" if a+b>c and b+c>a and c+a>b else "Not valid triangle"
    
vt = validTriangle()
a,b,c = map(int,input().split())
print(vt.validtri(a,b,c))
# print(vt.validtri(int(input("1st side")), int(input("2nd side")), int(input("3rd side"))))
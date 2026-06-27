# Take a character and check whether it’s uppercase, lowercase, a digit, or a special 
# character.


class Checkchar:
    def checkchar(self,c):
        return "Uppercase" if c.isupper() else "lowercase" if c.islower() else "digit" if c.isdigit() else "Special character"

cc = Checkchar()
print(cc.checkchar(input()))
#count the digits
import math
class count_digits:
    def count_digit(self,n):
        # brute force method
        # count = 0
        # while(n>0):
        #     rem = n%10
        #     count = count+1
        #     n = n //10
        # return count

        #better approach
        if n == 0:
            return 1
        else:
            return int(math.log10(n))+1

# sol = count_digits()
# n = int(input("Enter the number that you want to count\n"))
# print("The number of digits is: ",sol.count_digit(n))


class reversenumber:
    def reversenumber(self, n):
        #brute force
        rev = 0
        while(n>0):
            rem = n % 10
            rev = rev * 10 + rem
            n = n//10
        return rev

# rn = reversenumber()
# n = int(input("Enter the number that you want to reverse\n"))
# print("The reversed number is: ", rn.reversenumber(n))

class Palindrome:
    def ispalindrome(self, n):

        original = n
        rev = 0
        while(n>0):
            rem = n%10
            rev = rev * 10 +  rem
            n = n//10
        return rev == original

pal = Palindrome()
n = int(input("Enter the number that you want to test:\n"))
if pal.ispalindrome(n):
    print(f"The number {n} is plaindrome")
else:
    print(f"The number {n} is not plaindrome")
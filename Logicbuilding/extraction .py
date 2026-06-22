#count the digits
class Solution:
    def count_digit(self,n):
        count = 0
        while(n>0):
            rem = n%10
            count = count+1
            n = n //10
        return count

sol = Solution()
n = int(input("Enter the number that you want to count\n"))
print("The number of digits is: ",sol.count_digit(n))
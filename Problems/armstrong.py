class Solution:
    def isArmstrong(self, n):
        armstrong = False
        original = n 
        digits = len(str(n))
        sum = 0
        while n>0:
            rem = n%10
            sum += rem**digits
            n = n//10
        if sum == original:
            return True
        else:
            return False

sol = Solution()
armstrong = sol.isArmstrong(153)
if armstrong:
    print("Armstrong")  





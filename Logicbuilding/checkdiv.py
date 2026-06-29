class Solution:
    def divisible(self,n):
        if n%15==0:
            return True
        return False

sol = Solution()
if sol.divisible(int(input())):
    print("Divisible by 5")
else:
    print("Not Divisible by 5")
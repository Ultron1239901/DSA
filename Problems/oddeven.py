class Solution:
    def oddeven(self, n):
        if n%2==0:
            return "Even"
        else:
            return "Odd"
sol = Solution()
n = int(input())
print(sol.oddeven(n)) 
class Solution:
    def reverse(self, x):
        sign = -1 if x<0 else 1
        x = abs(x)
        rev = 0
        while x!=0:
            rem = x%10
            rev = rev*10 + rem
            x = x//10
        rev = rev*sign
        return rev

sol = Solution()
x = 123
print(sol.reverse(x)) 
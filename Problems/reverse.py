class Solution:
    def reverse(self, n):
        rev=0
        if n ==0:
            return 0
        while n>0:
            rem = n%10
            rev = rev*10 +rem
            n = n//10
            
        return rev
    
sol = Solution()
print(sol.reverse(1234))
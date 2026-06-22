class Solution:
    def fibonacci(self, n):
        if n <=0:
            return "Invalid input"
        if n ==1:
            return 0
        if n == 2:
            return 1
        a, b = 0, 1
        for i in range(3, n+1):
            a, b = b, a+b
        return b
    
sol = Solution()
n = int(input())
print(sol.fibonacci(n))
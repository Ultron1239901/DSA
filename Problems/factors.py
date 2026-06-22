class Solution:
    def factors(self, n):
        #brute force approach 
        l = []
        for i in range(1,(n//2)+1):
            if n%i ==0:
                print(i)
                l.append(i)
        l.append(n)
        return l
    
sol = Solution()
n = int(input("Enter the number to find the factors of:\n"))
print("The factors of the number ",n,"is",sol.factors(n))
            

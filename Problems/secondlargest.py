class Solution:
    def secondlargest(self, nums):
        first = second = float('-inf')
        for num in nums:
            if num > first:
                second = first 
                first = num
            
        return second
    
sol = Solution()
print(sol.secondlargest([1,2,3,4,5])) 



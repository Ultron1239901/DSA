# class Solution(object):
#     def twoSum(self, numbers, target):
#         exist = {}
#         for i in range(0,len(numbers)):
#             remaining = target - numbers[i]
#             if remaining in exist:
#                 return [exist[remaining],i]
#             exist[remaining] = i
    
# sol = Solution()
# numbers = [2,7,11,15] 
# target = 9
# print(sol.twoSum(numbers,target))
        

class Solution(object):
    def twoSum(self, numbers, target):
        i=0
        j=len(numbers)-1
        while i<j:
            sum = numbers[i] + numbers[j]
            if target==sum:
                return [i+1,j+1]
            elif target<sum:
                j=j-1
            else:
                i=i+1
        
               
    
sol = Solution()
numbers = [5,25,75]
target = 100
print(sol.twoSum(numbers,target))
        
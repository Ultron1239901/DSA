# class Solution:
#     def containsDuplicate(self, nums):
#         for i in range(0,len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]==nums[j]:
#                     return True
                
#         return False

# class Solution:
#     def containsDuplicate(self, nums):
#         seen = set()
#         for n in nums:
#             if n in seen:
#                 return True
#             seen.add(n)       
#         return False


class Solution:
    def containsDuplicate(self, nums):
        return False if len(nums)==len(set(nums)) else True
    

sol = Solution()
nums = [1,2,3,1]
print(sol.containsDuplicate(nums))
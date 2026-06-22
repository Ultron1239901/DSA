# # class Solution:
# #     def twoSum(self, nums,target):
# #         for i in range(0,len(nums)):
# #             for j in range(i+1,len(nums)):
# #                 if nums[i]+nums[j]==target:
# #                     return [i,j]

# def twoSum(nums, target):
#     seen = {}  # value -> index

#     for i, num in enumerate(nums):
#         needed = target - num
#         if needed in seen:
#             return [seen[needed], i]
#         seen[num] = i

                

# print(twoSum([1,2,3,4,5],6))

# nums = [-1,0,1,2,-1,-4]
# i=0
# j=1
# k=2
# while(k<len(nums)):
#     if i!=j and j!=k and i!=k:
#         if nums[i]+nums[j]+nums[k]==0:
#             print(nums[i],nums[j],nums[k])
#     i+=1
#     j+=1
#     k+=1

# a = 60
# b = 60
# # del(a)
# print(id(b))
# print(id(a))
# # print(id(c))


class Solution:
    def twosum(self, nums,target):
        n = len(nums)
        exist = {}
        for i in range(0,n):
            rem = target - nums[i]
            if rem in exist:
                return [exist[rem],i]
            exist[nums[i]] = i

sol = Solution()
arr = list(map(int, input().split()))
target = int(input())
print(sol.twosum(arr,target))

            

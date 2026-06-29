# class Solution:
#     def subarraySum(self, nums, k):

#         prefix_sum = 0
#         count = 0

#         hashmap = {0: 1}

#         for num in nums:

#             prefix_sum = prefix_sum + num
#             remaining = prefix_sum-k
#             if remaining in hashmap:
#                 count = count+ hashmap[remaining]

#             hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1
#         print(hashmap)
#         print(f"COunt is {count}")


# sol = Solution()

# nums = [1, 1, 1]
# k = 2

# sol.subarraySum(nums, k)

class Solution:
    def subarraySum(self, nums, k):
        prefix = [0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        print(prefix)
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i ==0:
                    total = prefix[j]
                else:
                    total = prefix[j]-prefix[i-1]
                if total == k:
                    count +=1
        print(count)

sol = Solution()

nums = [1, 1, 1]
k = 2

sol.subarraySum(nums, k)


        
        
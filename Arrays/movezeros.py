class Solution:
    def moveZeroes(self, nums):
        i = 0
        for j in range(0,len(nums)):
            if nums[j]!=0:
                nums[i],nums[j] = nums[j],nums[i]
                i=i+1

sol = Solution()
nums = [0,1,0,3,12]
sol.moveZeroes(nums)
print(nums)
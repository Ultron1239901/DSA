class Solution:
    def rotatek(self, nums, left, right):
        while left< right:
            nums[left], nums[right] = nums[right],nums[left]
            left +=1
            right-=1
        
nums = list(map(int,input().split()))
k = int(input("Enter the number of places to rotate"))
l = len(nums)
sol = Solution()
sol.rotatek(nums,0,l-k-1)
sol.rotatek(nums,k,l-1)
sol.rotatek(nums,0,l-1)
print(nums) 

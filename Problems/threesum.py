class Solution:
    def threesum(self, arr, target):
        result = set()
        n = len(arr)
        for i in range(0,n):
            myset = set()
            for j in range(i+1,n):
                third = -(arr[i]+arr[j])
                if third in myset:
                    temp = [arr[i],arr[j],third]
                    temp.sort()
                    result.add(tuple(temp))
                myset.add(arr[j])
        return [list(ans) for ans in result]
    
sol = Solution()
arr = list(map(int, input().split()))
target = int(input("Enter the target sum"))
sol.threesum(arr,target)
print(sol.threesum(arr,target))

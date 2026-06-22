class Solution:
    def missing(self, arr):
        n = len(arr)
        #using the formula
        # total = n * (n + 1) // 2
        # sum_of_arr = sum(arr)
        # return total - sum_of_arr

        # using the XOR operator
        xor1 = 0
        xor2 = 0
        for i in range(1, n + 1):
            xor1 = xor1^i
        for num in arr:
            xor2 = xor2^num
        return xor1 ^ xor2
    
sol = Solution()
arr = list(map(int, input().split()))
print(sol.missing(arr)) 

# arr = [2, 3, 5, 1, 0]

# n = len(arr)

# expected_sum = 

# actual_sum = sum(arr)

# print(expected_sum - actual_sum)
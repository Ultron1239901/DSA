class Solution:
    def isArmstrong(self, n):
        #brute force approach
        # digits = len(str(n))
        # total = 0
        # for ch in str(n):
        #     total += int(ch)**digits

        # if total==n:
        #     print("Arm strong number")
        # else:
        #     print("Not arm strong number")
        #better approach
        # armstrong = False
        # original = n 
        # digits = len(str(n))
        # sum = 0
        # while n>0:
        #     rem = n%10
        #     sum += rem**digits
        #     n = n//10
        # if sum == original:
        #     return True
        # else:
        #     return False
        

sol = Solution()
armstrong = sol.isArmstrong(152)
if armstrong:
    print("Armstrong")  





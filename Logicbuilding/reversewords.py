class Solution(object):
    def reverseWords(self, s):
        return s[::-1]

sol = Solution()
s = "the sky is blue"
print(sol.reverseWords(s))
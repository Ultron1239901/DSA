class Solution:
    def isPalindrome(self, x: int) -> bool:
        word = str(x)
        print(len(word))
        for i in range(len(word)//2):
            print(i)
            if word[i] != word[len(word)-i-1]:
                return False
        return True
        
        # return True if original == rev else False

sol = Solution()
x = 121 
print(sol.isPalindrome(x))
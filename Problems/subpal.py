s = input().strip()
start = 0
max_len = 1
def expand(left, right):
    global max_len,start
    while left>=0 and right<len(s) and s[left]==s[right]:
        curlen = right - left + 1
        if curlen > max_len:
            max_len = curlen
            start = left
        left -=1
        right +=1

for i in range(len(s)):
    expand(i,i)
    expand(i,i+1)
     
print(s[start:start+max_len])
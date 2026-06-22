def linearsearch(arr,target):
    for i in range(0,len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = list(map(int,input().split()))
print(arr)
target = int(input())
ele = linearsearch(arr,target)
if ele ==-1:
    print("Element not found")
else:
    print("Element found at the index",ele)
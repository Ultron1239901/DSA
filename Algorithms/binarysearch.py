def binarysearch(arr, target):
    low = 0
    high = len(arr)-1
    while low <=high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid-1
        elif target > arr[mid]:
            low = mid-1
    return -1

arr = list(map(int, input().split()))
target = int(input("Enter the target element: "))
ele = binarysearch(arr,target)
if ele == -1:
    print("Element not found")
else:
    print("Element found at the index",ele)

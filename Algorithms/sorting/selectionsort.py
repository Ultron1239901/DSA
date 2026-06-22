def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        minindex = i
        for j in range(i+1,n):
            if arr[j]<arr[minindex]:
                minindex = j 
        arr[i],arr[minindex] = arr[minindex],arr[i]

arr = list(map(int, input().split()))
selectionsort(arr)
print("Sorted array is:", arr) 
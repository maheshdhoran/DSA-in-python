#1 By Pointers
# Complexity Time- O(N)
def sort012(arr,n):
    low=0
    mid=0
    high=n-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            mid+=1
            low+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr
arr=[2,2,1,0,0,2,1,0]
print(sort012(arr,len(arr)))

#2 By using extra space
# Complexity Time- O(N) Space-O(N)
def sort012_2(arr):
    zero=[0]*(arr.count(0))
    one=[1]*(arr.count(1))
    two=[2]*(arr.count(2))
    return zero+one+two

arr=[2,2,1,0,0,2,1,0]
print(sort012_2(arr))
#1 By Sorting
# Complexity Time- O(NlogN)
def kth_smallest(arr,k):
    arr.sort()
    return arr[k-1]
arr=[55,23,1,5,3]
k=3
print(kth_smallest(arr,k))



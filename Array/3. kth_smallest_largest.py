#1 By Sorting
# Complexity Time- O(nlogn)
def kth_smallest(arr,k):
    arr.sort()
    return arr[k-1]
arr=[55,23,1,5,3]
k=3
print(kth_smallest(arr,k))

#2 By Sorting
# Complexity Time- O(nlogn)
def kth_largest(arr,k):
    arr.sort(reverse=True)
    return arr[k-1]
arr=[55,23,1,5,30]
k=2
print(kth_largest(arr,k))



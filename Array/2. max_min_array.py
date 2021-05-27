#1 By Linear Search
# Complexity Time- O(N)
def min_max(arr):
    min_val=arr[0]
    max_val=arr[0]
    for i in range(1,len(arr)):
        min_val=min(min_val,arr[i])
        max_val=max(max_val,arr[i])
    return max_val,min_val
arr=[23,15,66,78,-1]
max_val,min_val=min_max(arr)
print(max_val,min_val)
print()

#2 By Tournament Method
# Approach Divide and Conquer
# Complexity T(n)= 3n/2-2 comparisons if n is a power of 2 otherwise more comparisons
def min_max1(low,high,arr):
    max_val=arr[low]
    min_val=arr[low]

    if low==high:
        max_val=arr[low]
        min_val=arr[low]
        return max_val,min_val
    
    elif high==low+1:
        if arr[low]>arr[high]:
            max_val=arr[low]
            min_val=arr[high]
        else:
            max_val=arr[high]
            min_val=arr[low]
        return max_val,min_val

    else:
        mid=int((low+high)/2)
        max_val1,min_val1=min_max1(low,mid,arr)
        max_val2,min_val2=min_max1(mid+1,high,arr)
    return max(max_val1,max_val2) , min(min_val1,min_val2)

arr=[23,15,66,78,-1]
max_val,min_val=min_max1(0,len(arr)-1,arr)
print(max_val,min_val)
print()

#3 By Pair Comparisons
# Complexity  if n is odd 3*(n-1)/2 otherwise 3n/2-2
def min_max2(arr):
    n=len(arr)

    if n%2==0:
        min_val=min(arr[0],arr[1])
        max_val=max(arr[0],arr[1])
        i=2
    else:
        min_val=max_val=arr[0]
        i=1
    
    while(i<n-1):
        if arr[i]>arr[i+1]:
            max_val=max(max_val,arr[i])
            min_val=min(min_val,arr[i+1])
        else:
            max_val=max(max_val,arr[i+1])
            min_val=min(min_val,arr[i])
        i=i+2
    return max_val,min_val
arr=[23,15,66,78,-1]
max_val,min_val=min_max2(arr)
print(max_val,min_val)
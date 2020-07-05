#complexity of code O(logn)
#Using Iteration

arr=[1,2,3,4,5,55,66,77,78,79,88,89,90,93,99]

def binary(arr,n):
    lowerBound=0
    upperBound=len(arr)-1
    
    while lowerBound<=upperBound:
        
        mid=(lowerBound+upperBound)//2
        
        if arr[mid]==n:
            return mid
            
        elif n<arr[mid]:
            upperBound=mid-1
            
        elif n>arr[mid]:
            lowerBound=mid+1
    else:
        return 0
        
print(binary(arr,99))
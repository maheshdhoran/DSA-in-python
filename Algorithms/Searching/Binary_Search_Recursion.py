#complexity of code O(logn)
#Using Recursion

arr=[1,2,3,4,5,55,66,77,78,79,88,89,90,93,99]
lowerBound=0
upperBound=len(arr)-1

def binary(arr,n,lowerBound,upperBound):
    
    if lowerBound<=upperBound:
        
        mid=(lowerBound+upperBound)//2
        
        if arr[mid]==n:
            return mid
            
        elif n<arr[mid]:
            return binary(arr,n,lowerBound,mid-1)
            
        elif n>arr[mid]:
            return binary(arr,n,mid+1,upperBound)
    else:
        return 0
        
print(binary(arr,99,lowerBound,upperBound))
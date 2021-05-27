#1 Partition process of quick sort
# Complexity Time- O(N)
def move_negative_array_elements(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr
arr=[-1, -5, -6, 3, 98, 45, -33]
print(move_negative_array_elements(arr))
print()

#2 By pointers
# Complexity Time- O(N)
def move_negative_array_elements1(arr):
    i=0
    j=len(arr)-1

    while i<=j:
        if arr[i]<0 and arr[j]<0:
            i+=1
        elif arr[i]>0 and arr[j]<0:  #Our Main Condition
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        elif arr[i]>0 and arr[j]>0:
            j-=1
        else:
            i+=1
            j-=1
    return arr
arr=[-1, -5, -6, 3, 98, 45, -33]
print(move_negative_array_elements1(arr))
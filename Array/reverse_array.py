#1 Two pointer approach
#Complexity Time- O(n)
def reverse_array1(arr):
    i=0
    j=len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

arr=[1, 2, 3, 4, 5]
print(arr)
print(reverse_array1(arr))

#2 Two pointer approach using recursion
#Complexity Time- O(n)
def reverse_array2(arr,i,j):
    if i>=j:
        return
    arr[i],arr[j]=arr[j],arr[i]
    reverse_array2(arr,i+1,j-1)

arr=[1, 2, 3, 4, 5]
print(arr)
reverse_array2(arr,0,len(arr)-1)
print(arr)

#3 Using extra space
#Complexity Time- O(n), Space- O(n)
def reverse_array3(arr):
    arr2=[None]*(len(arr))
    j=0
    for i in range(len(arr)-1,-1,-1):
        arr2[j]=arr[i]
        j+=1
    return arr2

arr=[1, 2, 3, 4, 5]
print(arr)
print(reverse_array3(arr))


#4 Using python slicing
#Complexity Time- O(n)
def reverse_array4(arr):
    return arr[::-1]

arr=[1, 2, 3, 4, 5]
print(arr)
print(reverse_array4(arr))

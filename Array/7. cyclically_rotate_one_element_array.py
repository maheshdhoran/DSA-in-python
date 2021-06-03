#1 Shift elements to right
#Complexity O(n)
def array_shift_by_one(arr):
    main_element=arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=main_element
    return arr

arr=[3, 6, 1, 2, 8]
print(array_shift_by_one(arr))
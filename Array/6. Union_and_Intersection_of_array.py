#1 Union of sorted arrays(without handling duplicates by using merge procedure)
#Complexity O(m+n)
def union_sorted_with_duplicates(arr1, arr2):
    i,j=0,0
    m,n=len(arr1),len(arr2)
    while i<m and j<n:
        if arr1[i] < arr2[j]:
            print(arr1[i], end=" ")
            i+=1
        elif arr2[j] < arr1[i]:
            print(arr2[j], end=" ")
            j+=1
        else:
            print(arr1[i], end=" ")
            i+=1
            j+=1
    while i<m:
        print(arr1[i], end=" ")
        i+=1
    while j<n:
        print(arr2[j], end=" ")
        j+=1

arr1=[2, 3, 6, 8, 9]
arr2=[1, 2, 7, 7]
union_sorted_with_duplicates(arr1, arr2)
print()
print()

#2 Union of unsorted arrays by using sets
# Complexity O(m+n)
def union_unsorted(arr1, arr2):
    s=set()
    for i in arr1:
        s.add(i)
    for j in arr2:
        s.add(j)
    print(s)
arr1=[10, 6, 2, 3, 6, 8, 9]
arr2=[9, 1, 2, 7, 7]
union_unsorted(arr1, arr2)
print()


#3 intersection of unsorted arrays (without handling duplicates by using merge procedure)
# Complexity O(m+n)
def intersection_sorted(arr1, arr2):
    i,j=0,0

    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr1[i]:
            j+=1
        else:
            print(arr1[i], end=" ")
            i+=1
            j+=1

arr1=[2, 3, 6, 7, 8, 9]
arr2=[1, 2, 7, 7]
intersection_sorted(arr1, arr2)
print()
print()

#4 intersection of unsorted arrays by sets
# Complexity O(m+n) Space O(n)
def intersection_unsorted(arr1, arr2):
    s=set()
    for i in arr1:
        s.add(i)
    for j in set(arr2):
        if j in s:
            print(j, end=" ")
arr1=[10, 6, 2, 3, 6, 8, 9, 7]
arr2=[9, 6, 1, 2, 7, 7]
intersection_unsorted(arr1, arr2)
print()
    
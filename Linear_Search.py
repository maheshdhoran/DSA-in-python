#complexity of code O(n)

arr=[1,2,3,4,5,55,66,77,78,79,88,89,90,93,99]

def lise(arr,n):
    for i in arr:
        if i==n:
            return arr.index(i)

print(lise(arr,88))
#1 using Kadane's Algorithm
# Complexity O(n)

def largest_sum_contiguous_subarray(arr):
    max_sum=arr[0]
    summ=0
    for i in range(len(arr)):
        summ=summ+arr[i]
        if max_sum < summ:
            max_sum = summ
        if summ < 0:
            summ=0
    return max_sum

arr=[8, 3, 6, -3, 0, 9, -4, -5]
print(largest_sum_contiguous_subarray(arr))
print()

# Printing Largest sum contiguous subarray
def largest_sum_contiguous_subarray(arr):
    max_sum=arr[0]
    summ=0
    start=0
    end=0
    s=0
    for i in range(len(arr)):
        summ=summ+arr[i]
        if max_sum < summ:
            max_sum = summ
            start=s
            end=i
        
        if summ < 0:
            summ=0
            s=i+1
    return max_sum,start,end

arr=[8, 3, 6, -3, 0, 9, -4, -5]
max_sum,start,end=largest_sum_contiguous_subarray(arr)
print(max_sum)
print(arr[start:end+1])

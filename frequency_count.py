# from collections import Counter

# def sorted_by_freq(arr):
#     freq = Counter(arr)

#     sorted_arr = sorted(arr, key=lambda y:(-freq[y], y))

#     return sorted_arr

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = sorted_by_freq(arr)
#     print(" ".join(map(str,result)))



def merge_sort(arr, freq):
    # If the array has 1 or no elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], freq)
    right_half = merge_sort(arr[mid:], freq)
    
    # Merge the two halves while sorting by frequency and value
    return merge(left_half, right_half, freq)

def merge(left, right, freq):
    result = []
    i = j = 0
    
    # Merge the two halves based on frequency and then value
    while i < len(left) and j < len(right):
        if (freq[left[i]] > freq[right[j]]) or \
           (freq[left[i]] == freq[right[j]] and left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append the remaining elements from both halves
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def sorted_by_freq(arr):
    # Step 1: Count frequencies manually
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Step 2: Use merge sort to sort the array based on frequency and value
    sorted_arr = merge_sort(arr, freq)

    return sorted_arr

# Taking input
T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    result = sorted_by_freq(arr)
    print(" ".join(map(str, result)))

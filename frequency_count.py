# from collections import Counter

# def sorted_by_freq(arr):
#     freq = Counter(arr)

#     sorted_arr = sorted(arr, key=lambda y:(-freq[y], y))

#     return sorted_arr


T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    result = sorted_by_freq(arr)
    print(" ".join(map(str,result)))



def merge_sort(arr, freq):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], freq)
    right_half = merge_sort(arr[mid:], freq)
    
    return merge(left_half, right_half, freq)

def merge(left, right, freq):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if (freq[left[i]] > freq[right[j]]) or \
           (freq[left[i]] == freq[right[j]] and left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def sorted_by_freq(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    sorted_arr = merge_sort(arr, freq)

    return sorted_arr


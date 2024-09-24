def merge_sorted_arr(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    i=0
    j=0
    L = []
    while i<n and j<m:
        if arr1[i]<arr2[j]:
            L.append(arr1[i])
            i += 1
        else:
            L.append(arr2[j])
            j += 1

    while i<n:
        L.append(arr1[i])
        i+=1

    while j<m:
        L.append(arr2[j])
        j+=1


    return L




arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.sort()
arr2.sort()
print(arr1)
print(arr2)
combined_arr = merge_sorted_arr(arr1,arr2)
print(combined_arr)



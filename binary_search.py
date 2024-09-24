def search_number(arr, n, l, r):
    if l>r:
        return -1
    mid = (l+r)//2

    if arr[mid]==n:
        return mid
    elif n<arr[mid]:
        return search_number(arr, n, l, mid-1)
    else:
        return search_number(arr, n, mid+1, r)


arr = list(map(int, input().split()))
n = int(input())

arr.sort()
print(arr)
r = len(arr) - 1

t = search_number(arr, n, 0, r)

if(t==-1):
    print("Number not found")
else:
    print(f"Number {n} present at {t} position.")
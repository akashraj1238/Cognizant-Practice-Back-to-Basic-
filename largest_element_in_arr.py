arr = list(map(int, input().split()))
maxi = arr[0]
for i in range(len(arr)):
    maxi = max(maxi, arr[i])

print(maxi)
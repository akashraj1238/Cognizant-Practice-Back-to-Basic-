arr = list(map(int, input().split()))

add=0
maxi=float('-inf')

for i in arr:
    add += i
    maxi=max(add, maxi)
    if add<0:
        add = 0
        
print(maxi)
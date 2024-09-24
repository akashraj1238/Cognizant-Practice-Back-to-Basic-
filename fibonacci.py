def fibo(num):
    if num==0:
        return 0
    if num==1:
        return 1
    return fibo(num-1) + fibo(num-2)


n = int(input())
L = []
for i in range(1,n+1):
    L.append(fibo(i))

print(L)


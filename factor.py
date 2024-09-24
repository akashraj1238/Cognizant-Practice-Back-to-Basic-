def print_factors(n):
    print(f"factors of {n} are: ")
    L = []
    for i in range(1, n+1):
        if n%i==0:
            L.append(i)
    
    print(L)

n = int(input())

print_factors(n)
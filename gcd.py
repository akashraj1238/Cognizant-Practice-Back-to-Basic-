def gcd(a,b):
    while b!=0:
        a,b=b, a%b

    return a

a = int(input())
b = int(input())

result = gcd(a,b)

print(f"GCD of {a} and {b} is: {result}")
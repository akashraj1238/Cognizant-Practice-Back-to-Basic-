d = int(input())

binary = ""

if d==0:
    print("0")

while d>0:
    rem = d%2
    binary = str(rem) + binary
    d //= 2

print(binary)

# n = str(input())
# sum=0
# for i in n:
#     sum+= int(i)

# print(sum)


n = int(input())

total = 0

while n>0:
    digit = n % 10
    total += digit
    n //= 10

print(total)


s = str(input())

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

count = 0

for i in s:
    if i in vowels:
        count += 1

print(count)

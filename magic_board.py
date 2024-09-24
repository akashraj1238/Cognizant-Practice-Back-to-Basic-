s = input()
if(s.isalpha()):
    ans = 0
    for i in s:
        ans+=ord(i)

    print(ans)
else:
    print("Error: Input should be only alphabets")

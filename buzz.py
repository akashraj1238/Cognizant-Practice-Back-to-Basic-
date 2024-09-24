n = int(input())
if n%7==0 or str(n).endswith('7'):
    print(f"{n} is a buzz number")
else:
    print(f"{n} is not a buzz number")
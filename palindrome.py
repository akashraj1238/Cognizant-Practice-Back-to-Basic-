def is_palindrome(n):
    str_num = str(n)
    return str_num == str_num[::-1]


n = int(input()) 

if n<0:
    print("Invalid Input")
elif is_palindrome(n):
    print("Palindrome")
else:
    print("Not a Palindrome")
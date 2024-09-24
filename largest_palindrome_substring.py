def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def largest_palindrome_substring(s):
    if len(s) == 0:
        return ""
    
    longest_palindrome = ""
    
    for i in range(len(s)):
        palindrome1 = expand_around_center(s, i, i)
        
        palindrome2 = expand_around_center(s, i, i + 1)
        
        longest_palindrome = max(longest_palindrome, palindrome1, palindrome2, key=len)
    
    return longest_palindrome

if __name__ == "__main__":
    string = input("Enter a string: ")
    
    result = largest_palindrome_substring(string)
    print(f"The largest palindrome substring is: '{result}'")


s1 = str(input())
s2 = str(input())

s1 = s1.replace(" ","").lower()
s2 = s2.replace(" ","").lower()

if sorted(s1)==sorted(s2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")
def swap_number(a,b):
    a = a+b
    b = a-b
    a = a-b

    return a,b

    
a = int(input("a = "))
b = int(input("b = "))

# a, b = b ,a

# print(a)
# print(b)

a,b = swap_number(a,b)

print("a = " + str(a))
print("b = " + str(b))

'''
5,3
5+3=8
8-5=3
8-3=5
'''
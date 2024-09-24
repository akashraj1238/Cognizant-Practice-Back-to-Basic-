n = int(input())

for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        
        for k in range(1, 2*i):
            print("*", end="")
        print()


for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("* " * i)



'''
    *
   ***
  *****
 *******
*********
'''


'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
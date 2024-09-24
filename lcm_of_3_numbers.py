def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1%num2
    return num1

def lcm(num1, num2):
    return abs(num1*num2)//gcd(num1, num2)

def lcm_of_three(num1,num2,num3):
    return lcm(lcm(num1,num2),num3)

if __name__ =="__main__":
    a = int(input())
    b = int(input())
    c = int(input())

    result = lcm_of_three(a,b,c)

    print(result)




'''
5,12
a    b
12 = 5*2 + (12%5)2
5  = 2*2 + (5%2)1
2  = 1*2 + (2%2)0
1  = 0
'''

'''
lcm(a,b)*gcd(a,b) = a*b
'''
def total(a,b,c):
    a=abs(a)*100
    b=abs(b)*20
    c=abs(c)*10
    return a+b+c

pizzas = int(input("Enter the number of pizzas bought: "))
puffs = int(input("Enter the number of puffs bought: "))
cool_drinks = int(input("Enter the number of cool drinks bought: "))
print("Number of pizzas: " + str(abs(pizzas)))
print("Number of puffs: " + str(abs(puffs)))
print("Number of cool_drinks: " + str(abs(cool_drinks)))
total_bills = total(pizzas, puffs, cool_drinks) 
print("Total Price: " + str(total_bills))
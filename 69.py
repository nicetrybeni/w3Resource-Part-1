# sort 3 integers using conditional statements and loops

x = int(input("Input 1st num: "))
y = int(input("Input 2nd num: "))
z = int(input("Input 3rd num: "))

a1 = min(x,y,z)

a3 = max(x,y,z)

a2 = (x+y+z) - a1 - a3

print(a1,a2,a3)
# convert distance in feet to inches,yars, and miles

d_ft = int(input("Input distance: "))

d_inches = d_ft * 12

d_yards = d_ft / 3.0

d_miles = d_ft / 5280.0

print(d_inches)
print(d_yards)
print(d_miles)
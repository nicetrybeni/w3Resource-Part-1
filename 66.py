# calculate bmi

height = float(input("input height"))
weight = float(input("input weight"))

bmi = weight / (height * height)
rounded_bmi = round(bmi, 2)

print("Your BMI is: ", rounded_bmi)
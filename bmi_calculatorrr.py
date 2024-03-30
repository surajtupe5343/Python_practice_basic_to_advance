name = input("Enter your name: ")
height_m = float(input("Enter your height: "))
weight_kg =int(input("Enter your weight: "))

def bmi_calculater(nm,ht,wt):
    bmi = wt/(ht**2)
    print("BMI: ")
    print(bmi)
    if bmi<25:
        return nm + " is not overweight"
    else:
        return nm + " is overweight"
print(bmi_calculater(name,height_m,weight_kg))
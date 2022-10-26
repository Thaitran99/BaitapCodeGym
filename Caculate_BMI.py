import math
weight = float(input(" Enter your weight"))
height = float(input("Enter your height"))
BMI = weight / (math.pow(height,2))
if BMI <16:
    print("Gầy cấp độ III")
elif BMI >=16 and BMI <17:
    print(" Gầy cấp độ II ")
elif BMI >=17 and BMI <18.5:
    print(" Gầy cấp độ I ")
elif BMI >=18.5 and BMI <25:
    print(" Bình thường ")
elif BMI >=25 and BMI <30:
    print(" Thừa cân ")
elif BMI >=30 and BMI <35:
    print(" Béo phì cấp độ I ")
elif BMI >=35 and BMI <40:
    print(" Béo phì cấp độ II ")
else :
    print(" Béo phì cấp độ III ")
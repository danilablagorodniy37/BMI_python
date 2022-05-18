# Body Mass Index
import math

weight = float(input('UR weight (kg): '))

growth = float(input('UR growth (m) : '))

BMI = round(weight / (growth * growth))
print('ur BMI: ' + str(BMI))
if BMI <= 18.5:{
        print('underweight')
    }
elif 18.5 <= BMI <= 24.9:{
        print('normal weight')
    }
elif 25 <= BMI <= 29.9:{
        print('overweight')
    }
elif 30 <= BMI <= 34.9:{
        print('preobesity')
    }
else:
    print('obesity')

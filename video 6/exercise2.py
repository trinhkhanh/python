__author__ = 'trinhkhanh'
weight = float(input('weight(pound): '))
height = float(input('height(inch): '))
BMI = (weight * 0.45359237)/(height*0.0254)**2
if BMI >= 18.5:
    if BMI < 25:
        print('normal')
    else:
        if BMI == 25 and BMI < 30:
            print('overweight')
        else:
            print('obese')
else:
    print('underweight')


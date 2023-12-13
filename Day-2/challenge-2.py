weight_str = input('Please enter your weight in kg... ')
height_str = input('Ok now please enter your height in m... ')

weight = float(weight_str)
height = float(height_str)

BMI = round((weight) / (height ** 2), 2)

if( BMI < 18.5 ):
    BMI_status = "Under-weight"
elif BMI > 18.5 and BMI < 25:
    BMI_status = "Normal-weight"
elif BMI > 25 and BMI < 30:
    BMI_status = "Over-weight"
else:
    BMI_status = "Obese"

BMI_str = str(round((weight) / (height ** 2), 2))



print('your BMI index is: ' + BMI_str + ' and your are ' + BMI_status)
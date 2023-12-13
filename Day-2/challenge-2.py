weight_str = input('Please enter your weight in kg... ')
height_str = input('Ok now please enter your height in m... ')

weight = float(weight_str)
height = float(height_str)

BMI = round((weight) / (height ** 2), 2)

if BMI < 18.5:
    BMI_status = "Underweight"
elif 18.5 <= BMI < 25:
    BMI_status = "Normal weight"
elif 25 <= BMI < 30:
    BMI_status = "Overweight"
else:
    BMI_status = "Obese"

BMI_str = str(round((weight) / (height ** 2), 2))



# print('your BMI index is: ' + BMI_str + ' and your are ' + BMI_status)
print(f"Your BMI index is: {BMI_str} and you are {BMI_status}")
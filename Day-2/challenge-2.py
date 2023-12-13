weight_str = input('Please enter your weight in kg... ')
height_str = input('Ok now please enter your height in cm... ')

weight = float(weight_str)
height = float(height_str)

BMI = str(round((weight) / (height ** 2), 2))


print('your BMI index is: ' + BMI)
''''
input the weight and height of the participant
calculate the BMI of the participant
print out the BMI of the participant
determine and show the participant is underweight/normal weight/obese
'''

m = float(input('Please input your weight in kg')) # collect the data of weight
h = float(input('Please input your height in m')) # collect the data of height
BMI = m/h**2 # Use the formula to cauculate your BMI value
print (f'Your BMI is {BMI} ')  # output the result of BMI calculator

if BMI>30:
    print('You are obese')
if BMI<18.5:
    print('You are underweight')
else:
    print('You are normal weight')
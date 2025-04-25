# define the calculator function
def drug_dosage_calculator(m,D):
    # ensure the data here match the expected range
    if 10 <= m <= 100 and D.strip() == 'a' or 'b':
        # give value to the real dose of drug
        if D == 'a':
            dose = 120
        elif D == 'b':
            dose = 250


        # calculate the volume of paracetamol required.
        dosage = m*15
        volume = 5*dosage/dose
        return volume
    else:
         return None

# collect the data of weight and the strength of drug
weight = float(input('Please enter your between 10 and 100 kg'))
expected_dose = str(input('Please choose your expected strength of paracetamol (a or b): a) 120 mg/5 ml b) 250 mg/5 ml):'))

# output the result
if drug_dosage_calculator(weight,expected_dose) is not None:        
        print(f'The volume needed here is {drug_dosage_calculator(weight,expected_dose)} ml')
else:   # report the error and remind to check
        print('Outlier, please check and enter again!')


# create a new python class
class Patient :
    def __init__ (self,name,age,admission_date,medical_history): # initialize a new patient with given attributes
        # set the attributes of name, age, admission date, medical history
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.medical_history = medical_history

    def print_record (self):
        print(f"name: {self.name}, age: {self.age}, date of latest admission: {self.admission_date}, medical hisory: {self.medical_history}")
# add the information of the first 'patient'
patient1 = Patient('Li Muxuan', 19, '8/4/2025', 'too clever')
patient1.print_record()
# add the information of the second 'patient'
patient2 = Patient('Xiang Yingzhe', 19, '9/4/2025', 'too lovely')
patient2.print_record()

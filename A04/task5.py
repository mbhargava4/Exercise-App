"""
PROBLEM 5
This file contains the code for problem 5 which asks us to make a class student which has 2 attributes namely last name and GPA"""
class student:
    def __init__(self):#default values for last name and GPA 
        self.lastName = "Popsecu"
        self.gpa = 3.8

    def set_lastName(self, lastName): #allows to set unique last name 
        self.lastName = lastName
        
    def set_gpa(self,gpa): #allows to set GPA
        if(gpa>4.0 or gpa<0):
            self.gpa = 3.8
        else:
            self.gpa = gpa
    

    def compareGPA(self, other): #compares GPA and outputs the last name of student wit higher GPA
        if(self.gpa>other.gpa):
            print(self.lastName)
        elif(self.gpa==other.gpa):
            print("Both have same GPA")
        else:
            print(other.lastName)




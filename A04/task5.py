class student:
    def __init__(self, lastName):
        self.lastName = "Popsecu"
        self.gpa = 3.8

    def set_lastName(self, lastName):
        self.lastName = lastName
        
    def set_gpa(self,gpa):
        if(gpa>4.0 or gpa<0):
            self.gpa = 3.8
        else:
            self.gpa = gpa
    

    def compareGPA(self, other):
        if(self.gpa>other.gpa):
            print(self.lastName)
        elif(self.gpa==other.gpa):
            print("Both have same GPA")
        else:
            print(other.lastName)




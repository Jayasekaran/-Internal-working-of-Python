class Person(): 
    def __init__(self, name, age, position): 
        self.name = name 
        self.age = age
        self.position = position

        print('Employee created.') 

    def __del__(self): 
       print('Destructor called, Employee deleted.')  
   
    def getEmployee(self): 
        return self.name ,self.age, self.position
   
    def isEmployee(self): 
        return False
   
   
# Inherited or Sub class 
class Employee(Person): 
   
    def isEmployee(self): 
        return True
   
# Driver code 
emp = Person("John",30, "Engineer")  # An Object of Person 
print(emp.getEmployee(), emp.isEmployee()) 
   
emp = Employee("Sam",36, "Engineer") # An Object of Employee 
print(emp.getEmployee(), emp.isEmployee())

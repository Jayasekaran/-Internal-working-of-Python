# functions and labmda functions
 
 #1 functions
def ask_user():
    print("Hello World")
 
# Function that returns sum
# of first 10 numbers
def my_func(b):
    a = b
    for i in range(1, 11):
        a = a + i
    return a
     
# Calling functions
ask_user()
res = my_func(0)
print(res)

#2 labmda function  
 
# Cube using lambda
cube = lambda x: x*x*x  
print(cube(7))
 
# List comprehension using lambda
a = [(lambda x: x * 2)(x) for x in range(5)]
print(a)
# Data Types  
# 1. Numeric  
   
print("Type of a: ", type(5))    
print("\nType of b: ", type(5.0))    
c = 2 + 4j
print("\nType of c: ", type(c)) 

#2. Dictionary  
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Dictionary', 'name':'key-value pair', 
        'A' : {1 : 'Dictionary', 2 : 'unordered ', 3 : 'collection'},
       }  
# accessing a element using key
print(Dict['name'])  
# accessing a element using get()
print(Dict.get(3)) 
     
# using pop()  
Dict.pop(5) 
print(Dict)  
 
# using popitem()  
Dict.popitem() 
print(Dict) 

#3. Boolean type 
   
print(type(True)) 
print(1>2)
print('a'=='a')

#4 .Set in Python  
set1 = set()
     
# Adding to the Set using add() 
set1.add(8)
set1.add((6, 7))
print(set1)  
   
# Additio to the Set using Update()   
set1.update([10, 11])
print(set1) 
 
#2. Sequence   
# String  
print('Hello World - String with single quotes')     
print("String with double quotes")
print('''I'm in "Python" world ''')
   
# Creating a List  
List = []  
print(List)  
     
# List 
List = ['Hello', 'World'] 
print(List)  
List = [['Hello', 'World'], ['Python']]  
print(List)

List = ['Hello', 'World'] 
    # append()
List.append(1)  
List.append(2)
print(List)  
   
    # insert()
List.insert(3, 12)  
List.insert(0, 'Great')
print(List)  
   
    # extend()  
List.extend([8, 'Great', 'Always'])  
print(List)

# Tuple  
Tuple1 = () #empty
print (Tuple1)  
     
    # tuple of strings 
print(('Great', 'Of'))  
     
    # Tuple of list  
print(tuple([1, 2, 4, 5, 6]))
 
# nested Tuple
Tuple1 = (0, 1, 2, 3)  
Tuple2 = ('python', 'great')  
Tuple3 = (Tuple1, Tuple2)
print(Tuple3)

#del tuple1[2] 

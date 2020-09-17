#Decision Making
#1. if and if-else
a = 10
b = 15
 
if a % 2 == 0:
    print("Even Number")
if b % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#2. while and while-else loop
i = 0
while (i < 3):      
    i = i + 1
    print("Hello World")  
    
a = [1, 2, 3, 4] 
while a: 
    print(a.pop()) 
   
i = 10
while i < 12:  
    i += 1
    print(i)  
    break
else: # Not executed as there is a break  
    print("No Break") 

# 3. Iterating using for loop
# Iterating over a list  
print("List Iteration")  
l = ["great", "programming", "language"]  
for i in l:  
    print(i) 
     
# Iterating over a String  
print("\nString Iteration")      
s = "Great"
for i in s :  
    print(i)  
     
print("\nFor-else loop")
for i in s:  
    print(i)  
else: # Executed because no break in for  
    print("No Break\n")  
   
for i in s:  
    print(i)  
    break
else: # Not executed as there is a break  
    print("No Break")  

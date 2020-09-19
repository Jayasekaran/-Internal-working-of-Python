# Internal of working in Python
This project provides basic and advanced concepts of Python. This project includes all topics of Python Programming such as icontrol statements, Strings, Lists, Tuples, Dictionary, Modules, Exceptions, Date and Time, File I/O, Programs, etc. 
It has example to Object Oriented programming approach to understand develop applications. It is simple and easy to learn and provides lots of high-level data structures.
Also Python interview questions added in this.

## Provides the following concepts:
### Data Types
Variables can hold values, and every value has a data-type. Python interpreter will automatically interpret variable as an integer type.

### Standard data types
A variable can hold different types of values. For example, a person's name must be stored as a string whereas its id must be stored as an integer.

Python provides various standard data types that define the storage method on each of them. The data types defined in Python are given below.
* **Numbers**
 *  **Integer**
  Its value belongs to int and there is no restriction on the length
 *  **Float**
  Float is used to store floating-point numbers like 1.9, 9.902, 15.2, etc.  and     the accurate is upto 15 decimal points
 *  **Complex** 
  A complex number contains an ordered pair, i.e., x + iy
*  ** Sequence Type**
 *  **String**
  The string can be defined as the sequence of characters represented in the quotation marks
  *  **List**
  Lists are enclosed within square brackets [] and it is similar to arrays in C
  
  ```python
  # Create List 
  lst  = [1, "welcome","to" "Python", 2]    
  #Checking type of given list  
  print(type(lst))
  #Printing the lst  
  print (lst)
  # List slicing
  print (lst[3:])
  # List slicing  
  print (lst[0:2])   
  # List Concatenation using + operator  
  print (lst + lst)  
  ```
  *  **Tuple**
 Tuples are enclosed in parentheses () and contains the collection of the items of different data types. It is read only.
   ```python
    #Create the tuple  
    _tup  = ("hello", "world", 2)    
    # Checking type of _tup  
    print (type(_tup)) 
	#Printing the tuple  
    print (_tup)
    # Tuple slicing  
    print (_tup[1:])    
    print (_tup[0:1])    
   ```
   *  **Dictionary**
It is enclosed in the curly braces {} and it is an unordered set of a key-value pair of items. Key can hold any primitive data type, whereas value is an arbitrary Python object
      ```python
      # Creating dictionary with key-value pair of elements 
      d = {1:'C', 2:'C++', 3:'Python', 4:'none'}
      # Printing dictionary
      print (d) 
      # Accesing value using keys  
      print("1st name is "+d[1])   
      print("2nd name is "+ d[4])
      # Printing all Keys and values    
      print (d.keys())    
      print (d.values())    
      ```
  *  **Boolean**
   Boolean type provides True and False.
  *  **Set**
Set is  unordered collection of the data type and it is iterable, mutable, and has unique elements.

        ```python
        # Creating Empty set  
        set1 = set()  
        # Creating set with values 
        set2 = {'1', 2, 3,'Python'} 
        # Adding element to the set
        set2.add(10) 
        # Printing Set value  
        print(set2)
        # Removing element from the set  
        set2.remove(2)  
        print(set2)  
        ```

### Python operators
The operator can be defined as a symbol which is responsible for a particular operation between two operands. Python provides a variety of operators.
* **Arithmetic operators**
Operators are used to perform arithmetic operations between two operands
* **Comparison operators**
 Operators are used to comparing the value of the two operands and returns Boolean true or false accordingly
* ** Assignment operators**
Operators are used to assign the value of the right expression to the left operand
* **Logical operators**
Operators are used primarily in the expression evaluation to make a decision
* **Bitwise operators**
Operators perform bit by bit operation on the values of the two operands
* **Membership operators**
Operators are used to check the membership of value inside a Python data structure
* **Identity operators**
Operators are used to decide whether an element certain class or type.(is/is not)

## Indentation in Python
In Python, indentation is used to declare a block. If two statements are at the same indentation level, then they are the part of the same block.

## Control flow

Decision making allows us to run a particular block of code for a particular decision.

| Statement    |Description               |
| ------------   | ------------               |
|If Statement  | The if statement is used to test a specific condition. If the condition is true, a block of code (if-block) will be executed. |
|If - else Statement  |The if-else statement is similar to if statement except the fact that, it also provides the block of the code for the false case of the condition to be checked. If the condition provided in the if statement is false, then the else statement will be executed.    |
|Nested if Statement|Nested if statements enable us to use if ? else statement inside an outer if statement.    |


## Python Function
A function can be defined as the organized block of reusable code. We can divide a large program into the basic blocks called as function.

There are mainly two types of functions.

- **User-define functions -** The user-defined functions are those define by the user to perform the specific task.
- **Built-in functions -** The built-in functions are those functions that are pre-defined in abs(),all(),bin(), 

| Built-in functions    |Description               | Example |
| ------------   | ------------               | -------------- |
|abs()  |  return the absolute value of a number |  ```  abs(-20) ```is: ```20 ```|
|all()  |  accepts an iterable object and returns true if all items are iterable. |  ```  k = [1, 3, 4, 6] ```   <br/>```   all(k) ```is ``` True ```|
|bin()  |  return the binary representation of a integer |  ``` bin(10) ```   is:```   0b1010 ```  |
|bool() |  converts a value to boolean(True or False)  |  ```bool(1)```   is: ```  ```  ```  True```  ```  |
|bytes()|  return the bytes object |  ``` bytes("test message",  'utf-8') ```   is: ```  b ' test message' ```  |
|callable()  |  eturns true if the object passed appears to be callable, otherwise false. |  ``` x = 8 ``` <br />  ```  callable(x)```     is:  ```  False  ```  |
|exec()  |  execution of program (string , object code or large blocks of code |  ``` x = 8 ``` <br />  ```   exec('print(x==8)') ```   is: ```  True ```  |
|sum()  |  to get the sum of numbers of an iterable, i.e., list.  |  ```  sum([1, 2, 4], 10) ```   is ```   17 ```  |
|any()  |  returns true if any item in an iterable is true. Otherwise, it returns False |  ``` any([1, 2, 4])```   is```   True ```  |
|ascii()  |  returns a string containing a printable representation of an object |  ``` ascii('Pythön is interesting' ) ```   is ```   'Pyth\xf6n is interesting' ```  |
|bytearray()  |  returns a bytearray object and can convert objects into bytearray objects, or create an empty bytearray object of the specified size.|
|eval()  |  runs python expression(code) within the program |  ``` x = 8  ``` <br />  ```  eval('x + 1') ```   is```    9 ```  |  
|float()  |  returns a floating-point number from a number or string |  ``` (float("  -17.19\n") ```  is ```   -17.19 ```  |
|format()  |  returns a formatted representation of the given value |  ``` format(123.0, "d") ```   is ```   123 ```  |
|frozenset()  | returns an immutable frozenset object initialized with elements from the given iterable |  ``` frozenset(('m', 'r', 'o', 't', 's')) ```   is ```   frozenset({'o', 'm', 's', 'r', 't'}) ```  | 
|getattr()  |  returns the value of a named attribute of an object ||
|globals()  |  returns the dictionary of the current global symbol table ||
|lter()  |   It creates an object which can be iterated one element at a time and return an iterator object |  ``` lst = [1,2,3,4,5] ``` <br />  ``` lstIter = iter(lst) ``` <br />  ```     print(next(lstIter)) ```    is ```   1 ```  |
|len()  |   return the length  |  ``` a = 'Python' ``` <br />  ``` print(len(a))   is: 6 |
|list()  | creates a list  |  ``` String = 'python' ``` <br />  ```  print(list(String)) ```    is ```   ['p', 'y', 't', 'h', 'o', 'n'] ```  |
|locals()  |  returns the dictionary of the current local symbol table <br /> Symbol table is defined as a data structure which contains all the necessary information about the program. It includes variable names, methods, classes, etc.|  ``` ```  |
|memoryview()  |  returns a memoryview object of the given argument |  ``` bin(10) is: 0b1010```  |
|map()  |  return the binary representation of a integer |  ``` def calculateAddition(n): ``` <br />  ```     return n+n  ``` <br />  ```  ``` <br />  ``` numbers = (1, 2, 3, 4) ``` <br />  ``` result = map(calculateAddition, numbers) ``` <br />  ``` print(result)```   is: ```<map object at 0x7fb04a6bec18> ```|
|min()  | return the smallest item in an iterable or the smallest of two or more arguments|  ``` ```  |
|max()  | return the largest item in an iterable or the largest of two or more |  ``` ```  |
|next()  | retrieve the next item from the iterator |  ```  ```  |
|object()  | return a new featureless object. object is a base for all classes.  |  ``` obj = object()   ```  |
|oct()  | convert an integer number to an octal string.  |  ```  ```  |
|open()  | open file and return a corresponding file object. |  ```  ```  |
|help()  | to get help related to the object  |  ``` f = open("python.txt")   ```  |
|chr()  | to get a string representing a character which points to a Unicode code integer |  ```chr(97) is 'a' ```  |
|complex()  | convert numbers or string into a complex number |  ``` complex(1,2) is (1.5+2.2j) ```  |
|delattr()  | to delete an attribute from a class |  ```  ```  |
|dir()  | returns the list of names in the current local scope |  ``` print ( dir()) ```  |
|divmod()  | to get remainder and quotient of two numbers |  ```divmod(10,2)  is (5, 0)  ```  |
|enumerate()  | returns an enumerated object |  ``` result = enumerate([1,2,3]) ``` <br />  ```print(list(result))  is  [(0, 1), (1, 2), (2, 3)]  ```  |
|dict()  | creates a dictionary |  ``` result = dict(a=1,b=2) `` <br />  ```print(result)   is {'a': 1, 'b': 2}```  |
|filter()  | to get filtered elements |  ```  ```  |
|hash()  | to get the hash value of an object |  ```  ```  |
|set()  | to create a new set using elements passed  |  ```set('12')  is {'1', '2'}  ```  |
|hex()  | to generate hex value of an integer argument. |  ``` hex(1)   is 0x1 ```  |
|id()  | returns the identity of an object |  ```  id("Javatpoint") ```  |
|setattr()  | to set a value to the object's attribute |  ```  ```  |
|slice()  | to get a slice of elements from the collection of elements |  ``` slice(0,5,3) is slice(0, 5, 3) ```  |
|sorted()  |  to sort elements |  ``` sorted('Python') is ['P', 'y', 't', 'h', 'o', 'n'] ```  |
|input()  |  to get an input from the user |  ```  ```  |
|int()  | to get an integer value |  ```  ```  |
|isinstance()  |  to check whether the given object is an instance of that class |  ```  ```  |
|ord()  | returns an integer representing Unicode code point for the given Unicode character |  ``` ord('8') ```  |
|pow()  | to compute the power of a number |  ``` pow(4, -2) is 0.0625 ```  |
|print()  |  prints the given object to the screen or other standard output devices. |  ```  ```  |
|range()  | returns an immutable sequence of numbers starting from 0 by default, increments by 1 (by default) and ends at a specified number. |  ```  ```  |
|reversed()  |  returns the reversed iterator of the given sequence |  ```  ```  |
|round()  |  rounds off the digits of a number and returns the floating point number |  ``` round(6.6) is 7 ```  |
|issubclass()  | returns true if object argument(first argument) is a subclass of second class(second argument) | |
|str()  | converts a specified value into a string |  ```  ```  |
|tuple()  | to create a tuple object |  ```  ```  |
|type()  | returns the type of the specified object if a single argument is passed to the type() built in function |  ```  ```  |

## Lambda Functions
A lambda function is a small anonymous function. A lambda function can take any number of arguments.
``` 
x = lambda a, b : a * b
print(x(5, 6)) 
```  

## Generators
Generators are a special class of functions that simplify the task of writing iterators. Regular functions compute a value and return it, but generators *return* an iterator that returns a stream of values. Any function containing a *yield* keyword is a generator function. When you call a generator function, it doesn’t return a single value; instead it returns a generator object that supports the iterator. On executing the *yield* expression, the generator outputs the value of *i*, similar to a return statement. The big difference between *yield* and a *return* statement is that on reaching a *yield* the generator’s state of execution is suspended and local variables are preserved. On the next call to the generator’s __next__() method, the function will resume executing.
 ``` 
 def generate_ints(N):
   for i in range(N):
     yield i
  
  gen = generate_ints(3)
  print(next(gen))
  print(next(gen))
  print(next(gen))
 ``` 
 
 ```
 0
 1
 2
 ```
 
### Passing values into a generator
 simple way to pass values into a generator. yield became an expression, returning a value that can be assigned to a variable or otherwise operated on:

```
val = (yield i) 
 ```

## Classes and Objects

 ``` 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
 ``` 

**__init__() :** function is called automatically every time the class is being used to create a new object
**self :** self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
**del :** delete the properties of the object or object itself by using the del keyword.
 
#### Class ####
The class can be defined as a collection of objects. It is a logical entity that has some specific attributes and methods. 

#### Object #### 
Everything in Python is an object, and almost everything has attributes and methods. 

#### Method ####
The method is a function that is associated with an object.

#### Inheritance #### 
Inheritance is the most important aspect of object-oriented programming. It specifies that the child object acquires all the properties and behaviors of the parent object.

#### Encapsulation ####
Encapsulation is also an essential aspect of object-oriented programming. It is used to restrict access to methods and variables. In encapsulation, code and data are wrapped together within a single unit from being modified by accident.

#### Data Abstraction ####
Data abstraction and encapsulation both are often used as synonyms.

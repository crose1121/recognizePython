num1 = 42 #variable declaration, initialize integer
num2 = 2.3 #variable declaration, initialize float
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize tuple
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement, access value, list
pizza_toppings.append('Mushrooms') #add value to list
print(person['name']) #log statement, access value, dictionary
person['name'] = 'George' #access value, dictionary
person['eye_color'] = 'blue'#change value, dictionary
print(fruit[2]) #log statement, access value, tuple

if num1 > 45: # if statement
    print("It's greater") #log statement
else: #else statement
    print("It's lower") #log statement

if len(string) < 5: #if statement, length check
    print("It's a short word!") #log statement
elif len(string) > 15: #elif statement, length check
    print("It's a long word!") #log statement
else: #else statement
    print("Just right!") #log statement

for x in range(5): #for loop, range function
    print(x) #log statement
for x in range(2,5): #for loop, range function, start & finish parameters
    print(x) #log statement
for x in range(2,10,3): #for loop, range function, start, finish, and increment parameters
    print(x) #log statement
x = 0 #variable declaration, initialize integer
while(x < 5): #while loop with parameter
    print(x) #log statement
    x += 1 #change value of variable

pizza_toppings.pop() #list, remove value
pizza_toppings.pop(1) #list, remove 2nd index value

print(person) #log statement, dictionary
person.pop('eye_color') #remove value, dictionary
print(person) #log statement, dictionary

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #if statement
        continue #continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #if statement
        break #break

def print_hello_ten_times(): #function declaration
    for num in range(10): #for loop with range parameter
        print('Hello') #log statement

print_hello_ten_times() #function call

def print_hello_x_times(x): #function declaration, takes in argument
    for num in range(x): #for loop, range function, parameter x
        print('Hello') #log statement

print_hello_x_times(4) #function call

def print_hello_x_or_ten_times(x = 10): #function declaration, argument
    for num in range(x): #for loop, parameter
        print('Hello') #log statement

print_hello_x_or_ten_times() #function call
print_hello_x_or_ten_times(4) #function call, argument


""" #docstring (multi-line quote)
Bonus section
""" #docstring (multi-line quote)

# print(num3) #NameError: name <variable name> is not defined

# num3 = 72 #single line comment

# fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment

# print(person['favorite_team']) #KeyError: 'favorite_team'

# print(pizza_toppings[7]) #IndexError: list index out of range

#   print(boolean) #IndentationError: unexpected indent

# fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append'

# fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'
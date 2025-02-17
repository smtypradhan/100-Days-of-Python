

#functions with inputs --> arguments and parameteres 

def greet():
    print("hello angela")
    print("how do you do?")
    print("isn't the weather nice?")

greet()    

### functions that allows inputs

def greet_with_name(name): #here the (name) is the parameter. Name of the data that has been passed.
    print(f"Hello {name}")
    print(f"How do you do {name}")
    print(f"Isn't the weather nice {name}")

greet_with_name("Smty") #here "Smty" is the argument or the actual value of the data

#exercise.py

def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")

life_in_weeks(12)

#Functions with more than 1 input
#Positional Arguments

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in the {location}")
greet_with("Jack", "USA") #This is a positional argument

#def my_function(a,b,c):
    #Do this with a
    #Then do this with b
    #Finally do this with c
#my_function(a,b,c)

#Keyword Argument
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in the {location}")
greet_with(location="USA", name="Jack") #This is a keyword argument

#exercise2.py

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
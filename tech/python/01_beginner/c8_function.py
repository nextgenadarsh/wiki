""" Function """

def greet (name, age = 0):
    print(f"Welcome {name} to the Python world !")
    if(age > 18):
        print("You are an adult so allowed to party !")

greet("Adarsh Kumar", 41)
greet("Tanya Rajvanshi")
greet(age=90, name = 'Rohit')

# Pass copy of list
def immutable(names):
    names.append("Pankaj")
    print(names)
names = ["Rahul", "Tanya", "Suresh"]
immutable(names)

# Unknown number of arguments
def params(*params):
    print(params)
    for param in params:
        print(f"{param}")
params("Rahul", "Krishna", "Sujata")

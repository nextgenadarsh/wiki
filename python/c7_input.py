name = input('Please enter your name: ')
print(f"Welcome {name}")
age = input('What is your age? ')
age = int(age)
if(age > 18):
    print("Congratulations ! You can vote.")
else:
    print("Enjoy your life !")

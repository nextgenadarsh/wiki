age = 19
if(age > 18):
    print("You are an adult")
elif (age > 60):
    print("You are senior citizen.")
else:
    print("You are a kid")

names = ["Adya", "Adarsh", "Advika"]

if(names): # Check if names is not empty
    if("Adya" in names):
        print("Adya is super girl.")
    if("adya" not in names):
        print("adya is NOT super girl.")

if(not names):
    print("Names list is empty")
else:
    print("Names list is not empty")


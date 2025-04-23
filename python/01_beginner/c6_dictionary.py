person = {'name': 'Adarsh Kumar', 'age': 48, 'city': 'Pune' }
person['color'] = 'dark'
person['name'] = 'Adarsh Kumar Chaurasia'

print(f"Name: {person['name']}")
print(f"Color: {person['color']}")

del person['color']

print(f"Color: {person.get('color', 'No color assigned')}")
print(f"DOB: {person.get('dob')}")

for key, value in person.items():
    print(f"Key: {key} | Value: {value}")

if('name' in person.keys()):
    print(f"Person name is: {person['name']}")

for value in person.values():
    print(f"Value: {value}")


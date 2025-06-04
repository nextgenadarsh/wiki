names = ["Sumit", "Adarsh", "Tanya", "Rubina", "Manoj"]
for name in sorted(names):
    print(name)
for value in range(5): # 0, . . , 4
    print(value)
for value in list(range(1, 5)): # 1, . . , 4
    print(value)

counter = 0
while (counter < 20):
    counter += 1

    if counter % 2 == 0:
        continue
    if(counter > 8):
        break
    print(f"Couter is: {counter}")

pets = ['cat', 'dog', 'cat', 'elephant', 'tiger']
while 'cat' in pets:
    pets.remove('cat')
print(f"Allowed pets are: {pets}")

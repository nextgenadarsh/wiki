names = ["Adarsh", "Sumit", "Tanya", "Roshan", "Kiran", "Nilam", "Raj"]
print(names)
names.append("Suresh")
names.insert(1, "Brijesh")
print(names)
del names[1]
print(names)
print(f"Removing name: {names.pop()}")
print(f"Removing name at index 2: {names.pop(2)}")
names.remove("Nilam")
print(names)
names.sort(reverse=True)
print(names)

# Sort and print without sorting actual array
print(sorted(names, reverse=False))
names.reverse()
print(names)
print(f"Total names: {len(names)}")
print(f"Last name is: {names[-1]}")

# even numbers
print(f"Even numbers: {list(range(2, 10, 2))}")
odd_numbers = list(range(1, 10, 2))
print(f"Odd numbers: {odd_numbers} | min: {min(odd_numbers)} - max: {max(odd_numbers)} - sum: {sum(odd_numbers)}")

squars = [value ** 2 for value in range(1, 10)]
print(squars)
print(f"First 3 names: {names[0:3]}")
print(f"First 3 names: {names[:3]}")
print(f"Names except first 2: {names[2:]}")
print(f"Last 2 names: {names[-2:]}")
copy_names = names[:]
print(f"Copied names: {copy_names}")


## Tuple

location = (400, 547)
print(location)

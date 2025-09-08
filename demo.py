n = int(input("Enter N: "))
total = sum(range(1, n+1))
print("Sum:", total)

# Program to demonstrate set operations
s = set()
count = int(input("How many elements to add to the set? "))
for _ in range(count):
    elem = input("Enter element: ") 
    s.add(elem)
print("Set:", s)



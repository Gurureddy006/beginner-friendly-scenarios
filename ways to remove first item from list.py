# Remove the first item from a list

a = ["Guru", 10, 20, 30, 40]
b = ["Ganesh", 50, 60, 70, 80]
c = ["Shiva", 100, 200, 300, 40]

# using remove method
a.remove("Guru")
print(a)
print()

# using pop method
b.pop(0)
print(b)
print()

# using del keyword
del c[0]
print(c)
print()

# using indexing
print(c[1:])
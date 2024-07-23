# Get unique values from a list in python without using set function

list1 = [1,3,5,4,5,7,5,4]
list2 = []
print(list1)

for val in list1:
    if val not in list2:
        list2.append(val)
print(list2)
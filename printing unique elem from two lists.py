# Get difference between two lists with Unique Entries

list1 = ['guru','ram','shiva','krishna']
list2 = ['guru','ram']

# One way
res = list(set(list1) - set(list2))
print(res)

# Another way

result = [val for val in list1 if val not in list2]
print(result)
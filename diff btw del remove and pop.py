# Difference between del, remove, and pop on lists

# 1. remove method removes the first matching value, not a specific index
a = [0,3,4,5,3]
print("Before removing :",a)

a.remove(3) # First occurence of 3 will be removed from list
print("After removing :",a)


# 2. del removes the item at a specific index
b = [0,1,3,7,2]
print("Before deleting :",b)

del b[2] # This remove element at index 2 which is 3
print("After deleting :",b)


# 3. pop also removes the item at a specific index
c = [2, 3, 4, 5]
print("Before removing :",c)

c.pop(2) # remove element at index 2 which is 4
print("After removing :",c)
# dispalying both uppper case and lower case alphabets using ascii values

import string as str

# ascii of lower case letters
b = str.ascii_lowercase
print("Lower case letters :",list(b))
res = b.replace('',' ').split()
new_list = []
for i in res:
    new_list.append(ord(i))
print(new_list)


# ascii of upper case letters
b1 = str.ascii_uppercase
print("Upper case letters :",list(b1))
res1 = b1.replace('',' ').split()
new_list1 = []
for i in res1:
    new_list1.append(ord(i))
print(new_list1)

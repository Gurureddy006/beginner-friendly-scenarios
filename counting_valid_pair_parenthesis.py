# Count no of valid pair of parenthesis in a list.

a = ['(',')','(','(',')',')']
count = 0
for i in range(len(a)):
    if a[i] == "(" and a[i+1] == ')':
        count += 1
print("No of valid pairs :",count)
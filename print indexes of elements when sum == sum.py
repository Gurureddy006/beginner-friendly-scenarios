# Printing index of those two elements(which is immediate next to another) where sum == given sum.

i = [1,2,3,5,4,6]
for ele in range(len(i)-1):
    if i[ele] + i[ele+1] == 9:
        print(f"{ele} , {ele+1}")

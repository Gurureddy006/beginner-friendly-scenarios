#  For a given array, write a program to print k smallest elements.Array is [1, 23, 17, 9, 32, 2, 50], k = 2

a = [12, 23, 17, 19, 32, 2, 50]
k = 3
for i in range(len(a)):
    res = sorted(a)
print(res)
print(res[:k]) # [2, 12, 17] - Increasing order

# To get an output in decreasing order
print(res[::-1][-k::]) # [17, 12, 2]
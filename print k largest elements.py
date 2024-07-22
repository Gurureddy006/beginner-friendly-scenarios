# For a given array, write a program to print k largest elements.Array is [1, 23, 17, 9, 32, 2, 50], k = 3.

a = [1, 23, 17, 9, 32, 2, 50]
k = 3
for i in range(len(a)):
    res = sorted(a)
print(res)
print(res[::-1][:k])
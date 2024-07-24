# Convert all strings in a list to integers in mutliple ways

# Method 1
a = ['1','2','3','4']
print(a)
res = []
for i in a:
    i = int(i)
    res.append(i)
print(res)


# Method 2
res1 = list(map(int,a))
print(res1)


# Method 3
res2 = [int(val) for val in a]
print(res2)

a = int(input("num :"))
count = 0
temp = a
while (temp>0):
    if (temp & 1) == 1:
        count += 1
    temp = temp >> 1
    
if (count == 0):
    print(0)
else:
    min = (1<<count)-1
    print("smallest integer :",min)
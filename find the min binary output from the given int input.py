# find the min binary output from the given integer input and conveert it into binary and then again to integer\

a = int(input("Number:"))
binary = bin(a)[2:]

count_zero = binary.count('0')
count_one = binary.count('1')

new_bin = '0'* count_zero + '1' * count_one
new_integer = int(new_bin,2)

print("smallest integer :",new_integer)

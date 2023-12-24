max_num = 0
for i in range (10):
    num = int(input(f"enter ur num for {i}:"))
    if num > max_num:
        max_num = num
print (f'max number is {max_num}')

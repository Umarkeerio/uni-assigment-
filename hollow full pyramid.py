i = 1
j = 6
while i <= 6:
    if i == 1 or i == 6:
        print(j * " " + "* " * i)
    else:
        print(j * " " + "* " + " " * (2 * (i - 2) - 1) + "*")
    i += 1
    j -= 1

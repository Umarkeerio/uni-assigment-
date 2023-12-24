num = int(input("enter ur num::"))
sum = 0
i = 1
while i<= num:
    sum  += i
    i += 1
print ('The sum of natural numbers up to',num,"is", sum)

#or
num = int(input("enter ur num::"))
sum = 0
while num > 0:
    sum += num
    num -= 1
print(f"sum,{sum}")

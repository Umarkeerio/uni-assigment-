#Exercise 1:
#Write a Python program that takes a number as input and prints "Even" if it's even and "Odd" if it's odd.
number = int(input("enter number ::"))
if number % 2 == 0:
    print (f"{number} is even")
else:
    print(f"{number} is odd")
#Exercise 2:
#Create a program that checks if a user-inputted year is a leap year. Print the result accordingly.
year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
#    Exercise 3:
#Write a program that prompts the user to enter their age. If the age is 18 or above, print "You are an adult," otherwise print "You are a minor."
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
#Exercise 4:
#Create a simple login system. Ask the user to enter their username and password. If the username is "admin" and the password is "12345", print "Login successful," otherwise print "Login failed."
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Login failed")
#Exercise 5:
#Write a program that determines if a given number is positive, negative, or zero. Print the result accordingly.
num = float(input("Enter a number: "))

if num > 0:
    print("Positive number.")
elif num == 0:
    print("Zero.")
else:
    print("Negative number.")
#Exercise 6:
#Ask the user to enter three numbers. Find and print the maximum of the three numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print(f"The largest number is {largest}")
#Exercise 7:
#Create a grading system. Take a numeric score as input and print the corresponding grade (A, B, C, D, or F).
score = float(input("Enter your score: "))

if score >= 90:
    print("Your grade is A.")
elif score >= 80:
    print("Your grade is B.")
elif score >= 70:
    print("Your grade is C.")
elif score >= 60:
    print("Your grade is D.")
else:
    print("Your grade is F.")
#Exercise 8:
#Write a program to check if a user-inputted number is a prime number or not. Print the result
import math

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
#Exercise 9:
#Create a program that checks if a user-inputted year is a leap year. If it is, print "Leap year," otherwise print "Not a leap year."
year = int(input("Enter a year: "))

if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
#Exercise 10:
#Prompt the user to enter two numbers. Print the larger number or a message saying they are equal.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is larger than {num2}")
elif num2 > num1:
    print(f"{num2} is larger than {num1}")
else:
    print("The numbers are equal")

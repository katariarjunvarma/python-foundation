# Problem 1 — Even or Odd
a = int(input("Enter a number: "))
if a % 2 == 0:
    print("The number you have given is an even number")
else:
    print("The number you have given is a odd")

# Problem 2 — Eligibility Check
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# PROBLEM 1: Number Sign Checker
a = int(input("Enter a number: "))
if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Zero")

# PROBLEM 2: Grade Calculator
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grdae B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

# PROBLEM 3: Largest of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter secound  number: "))
if a > b:
    print("first number is larger than secong number")
elif a < b:
    print("secound number is bigger than first number")
elif a == b:
    print("Both are equal")

# PROBLEM 4 (TRICKY): Login Check
a = input("Enter your username: ")
b = input("Enter your password: ")
if a == "admin" and b == "1234":
    print("Login Successful")
else:
    print("Login Failed")
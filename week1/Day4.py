# PROBLEM 1: Print Numbers
for i in range(1,11):
    print(i)

# PROBLEM 2: Even Numbers
for i in range(1,21):
    if i % 2 == 0:
        print(i)

# PROBLEM 3: Even Numbers
a=int(input("Enter your number: "))
for i in range(1,11):
    print(a,"x",i,"=",a * i)

# CODING PROBLEM 1: Count Even Numbers
n=int(input("Enter number: "))
for i in range(1,n + 1):
    if i % 2 ==0:
        print(i)

# CODING PROBLEM 2: Sum of Numbers
n=int(input("Enter number: "))
total=0
for i in range(1,n+1):
    total = total + i
print(total)

#  total = total + i
for i in range(1,6):
    print("*" * i)
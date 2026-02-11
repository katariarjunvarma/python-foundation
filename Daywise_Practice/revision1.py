# n = int(input("Enter a number: "))
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     print(i)


# n = int(input("Enter a number: "))
# total = 0
# for i in range(1, n + 1):
#     total = total + i
# print(total)


# for i in range(1,4):
#     for j in range(1,6):
#         print("*", end=" ")
#     print()


# for i in range(1,5):
#     for j in range(1, i + 1):
#         print(j, end = " ")
#     print()


# for i in range(4, 0, -1):
#     for j in range(1, i + 1):
#         print("*" ,end = "")
#     print()


# n = int(input("Enter a number: "))
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# for i in range(1, 11):
#     print(i)


# total = 0
# for i in range(1, 11):
#      total = total + i 
# print(total)


# for i in range(1, 5):
#     for j in range(1,i + 1):
#         print("*", end="")
#     print()


# for i in range(4, 0, -1):
#     for j in range(1, i +1):
#         print("*", end="")
#     print()


# for i in range(1,5):
#     for j in range(1, i +1):
#         print(j, end="")
#     print()


# n = int(input("Enter a number: "))
# print( n ** 2)
# print( n ** 3)
# print(type(n))


# n= int(input("Enter a number: "))
# if n > 0:
#     print("Positive")
# elif n < 0:
#     print("Negative")
# else:
#     print("Zero")


# n= int(input("Enter a number: "))
# for i in range(1, n + 1):
#     print(i)


# n= int(input("Enter a number: "))
# total = 0
# for i in range(1, n + 1):
#     total = total + i
# print(total)


# n= int(input("Enter a number: "))
# for i in range(1, n+1):
#     if i % 2 != 0:
#         print(i)

# for i in range(1,6):
#     for j in range (1, i +1):
#         print("*", end="")
#     print()


# n = int(input("Enter a number: "))
# for i in range(n, 0, -1):
#     if i % 2 ==0:
#         print(i)


word = "Arjun"
n = len(word)
for i in range(0 ,n):
    for j in range(0, i + 1):
        print(word[j], end = " ")
    print()
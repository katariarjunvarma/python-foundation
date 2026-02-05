# Program flow:
# Ask user for PIN
# If PIN is 1234:
# Show menu:
# 1. Check Balance
# 2. Withdraw
# 3. Exit
# Ask user to choose an option
# Based on choice:
# If 1 → print balance
# If 2 → ask withdrawal amount
# If amount ≤ balance → show remaining balance
# Else → print "Insufficient balance"
# If 3 → print "Thank you"
# If PIN is wrong → print "Wrong PIN"


a = int(input("Enter your PIN: "))
if a == 1234:
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")
    b = int(input("Choose an option: "))
    if b == 1:
        print("your balance is 5000")
    elif b == 2:
        c = int(input("Enter your withdrawl amount: "))
        if c <= 5000:
            print("Your remaining balanve is", 5000 - c)
        else:
            print("Insufficient balance")
    elif b == 3:
        print("Thank you")
    else:
        print("Invalid Input")
else:
   print("Wrong PIN")
x = int(raw_input("Input a number to check if it is even or odd: "))
if x%2 == 0:
    if x != 0:
        print("Your number is even.")
    else:
        print("Zero is neither even nor odd.")
else:
    print("Your number is odd.")

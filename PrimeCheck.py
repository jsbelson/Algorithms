import sys
x = int(raw_input("Insert a number: "))
if x > 1:
    for i in range (2,x):
        if x%i==0:
            print(str(x) + " is not prime.")
            sys.exit()
    print(str(x) + " is prime!")
else:
    print(str(x) + " is not prime.")

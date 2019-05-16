myList=[1,2,3,4,5,6,7,8,9]
x = int(raw_input("Enter a number: "))
print("You selected " + str(x) + ".")
for i in range (0, len(myList)):
    for j in range (0, len(myList)):
        if int(myList[i]+ myList[j]) == x:
            if int(myList[i]) != int(myList[j]):
                print(myList[i], myList[j])
#Jenny Belson

#for loop 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print("for:", x)

#The break statement
x = ["apple", "banana", "cherry"]
for x in fruits:
    print("break:", x)
    if x == "banana":
        break


#The continue statement
x = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print("continue:", x)   

for x in range(6):
    print("range:", x)

#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
    print("range with step:", x)


#Else in for loop
for x in range(6):
    print("else:", x)
else:
    print("Finally finished!")


    
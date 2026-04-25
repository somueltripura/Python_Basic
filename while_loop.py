# while loop

i = 1
while (i < 6):
    print("while:",i)
    i += 1

#The break statement
i = 1
while (i < 6):
    print("break:", i)
    i += 1
    if (i == 3):
        break
    i += 1

#The continue statement
i = 0 
while (i < 6):
    i += 1
    if (i == 3):
        continue
    print("continue:", i)


#The else statement
i = 1 
while (i < 6):
    print("else:", i)
    i += 1
else:
    print("i is no longer less than 6")

#The break statement with else
i = 1
while i < 6:
    if i == 3:
        break
    print("break with else:", i)
    i += 1
else:
    print("Done")

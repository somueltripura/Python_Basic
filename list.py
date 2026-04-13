#sort list of python

thislist = [100, 80, 60, 40, 20]

thislist.sort()
print(thislist)


#copy list
thislist = ["apple", "banana", "mango", "blackberry"]

mylist = thislist.copy()
print(mylist)


#Joint list
a = ["a", "b", "c"]
b = [1, 2, 3]
c = a + b
print(c)


#some contest
colors = ["red", "green", "purple",]
print(colors[0])
colors[1] = "yellow"
colors.append("blue")
colors.remove("red")
print(colors)
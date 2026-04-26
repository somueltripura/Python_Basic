#string formating of python

#এখানে f মানে f-string (formatted string)
#f-string ব্যবহার করলে তুমি string-এর ভিতরে variable বসাতে পারো

#👉 {price} এর জায়গায় Python নিজে থেকে 59 বসিয়ে দেবে

name = "Somuel"
age = 23
print(f"My first name is {name} and I am {age} years old.")


price = 49.99
print(f"The price of the item is {price} dollars.")

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

#Dictionary of python.

#git remote add origin https://github.com/somueltripura/Python-program.git
# git branch -M main
# git push -u origin main

#University System
student = {
    "name": "Somuel Tripura",
    "age": 23,
    "department": "CSE"
}
print(student)


#loging System(Username & Password)
user = {
    "somuel23": "pass23",
    "rahim": "abc234"
}


#E-commerce (Product price)
Products = {
    "Apple": 120,
    "Orange": 330,
    "Mango":100
}

print(Products)


#API data
response = {
    "status": 200,
    "data": {
        "name": "somuel",
        "email": "somueltripura@gmail.com",
        "phone": 1610227164
    }
}
print(response)

#change Item
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)
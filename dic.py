full_name = {"first": "John", "last": "Doe"}
person = {"name": "adjoda", "age": 30, "city": "New York"}

person["email"] = "john.doe@example.com"

 # Output: John

del person["city"]


#print(full_name["first"])

person.clear()
print(person) 
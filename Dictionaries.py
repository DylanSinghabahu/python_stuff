#We use dictionaries for storing information with key-value pairs


#Key   Value      These are key value pairs
#Name: John Smith
#Email: john@gmail.com
#Phone: 1234

customer = {
    "name": "Dylan",
    "age": 19,
    "is verified:": True

}

print(customer["age"])
#get method which uses parathensis
print(customer.get("birthdate", "Jan 1 1980")) #Doesn't give "KeyError:___" for missing values, instead returns "None"
#"Jan 1 1980" supplies a default value

print("-------------------")
profile = {
    "favourite_colour": "Blue",
    "favourite_food": "pie"
}
profile["favourite_food"] = "cake" #updates the favourite_food value
profile["phone"] = "0422963801" #adds new key-value pairs
print(profile["favourite_food"])
print(profile["phone"])
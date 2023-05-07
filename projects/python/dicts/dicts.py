# my_cat = ['Pixel', 0.25, 'Tonkinese', 'Chocolate Solid']
# my_cat = {'name': 'Pixel', 
#           'age': 0.25, 
#           'breed': 'Tonkinese', 
#           'colour': 'Chocolate Solid'}

# print(my_cat[2])

# if 'foo' in my_cat:
#     print(my_cat['foo'])
# else: 
#     print('Foo key not found')

# print(f"my cat {my_cat['name']} is a {my_cat['breed']}")

# print(my_cat.items())

# for key, value in my_cat.items():
#     print(f"{key} has the value: {value}")

# x = my_cat.pop('breed')
# print(x)
# print(my_cat)

# print(my_cat['breed']) #prints tonkinese but keeps it in the dict 
# print(my_cat.pop('breed')) # prints it and removes it from the dict, thanks to the pop() function

# del my_cat['breed'] #another way of removing the key-value pair from the dict 
# print(my_cat)

# my_cat['age'] = 42 #this is how we can change the value of a certain key in a dict
# print(my_cat)

# my_cat.update({'age': 42, 'name': 'penis'}) # this is another way of updating the values in a dict 
# print(my_cat)

# new_details = {'age': 42, 'name': 'penis', 'weight': '5kg'} #we can even store the updates in a variable, AND add more key value pairs 
# my_cat.update(new_details)
# print(my_cat)

people = [
    {'name': 'matt', 'age': 40},
    {'name': 'tom', 'age': 51},
    {'name': 'sam', 'age': 31}
]

# for person in people: 
#     print(f"{person['name']} is {person['age']} years old") #this iterates through people and returns the names and ages

#write a program to get a user input of a name. If that name is in the people list, print the details of that person, otherwise print an error message 

#PSEUDOCODE 
while True:
    #1. Get a name from the user 
    name = input('What name do you want to search for? (type nothing to exit) ')
    if name == '':
        break
    #2. Compare the name to the people list 
    found = False #using a flag, sets the default state of the flag, and later on if conditions are met this flag can be changed
    for person in people: 
        if person['name'].lower() == name.lower(): #makes both lower case so as to not break if users input a capital letter
            print(f"{person['name']} is {person['age']} years old")
            found = True #altering the flag 
            break

    #3. If the name is in the people list, print the details
    else: 
        print(f"{name} not found")
        age = int(input(f"what is the {name}'s age?")) #this will ask the user for the age of the person they just entered
        new_person = {'name': name, 'age': age} #this will take the name they just entered and the age and add it to a dict entry 
        people.append(new_person) #this adds that dict entry to the list of people
    #4. Else print an error 

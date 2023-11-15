'''Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the

owners name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 

each pet'''



pet1 = {'Kind':"Dog","Owner":"Johan"}
pet2 = {'Kind':"Cat","Owner":"Jerom"}
pet3 = {'Kind':"Parrot","Owner":"Satwick"}

pets = [pet1, pet2, pet3]

for pet in pets:
    kind = pet['Kind']
    owner = pet['Owner']
    print (f"The {kind} is owned by {owner}.")
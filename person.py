

# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
lista = [{ 'name': 'Mikko', 'age': 100, 'hobbies': ['HEMA', 'Playstation']}, 
         {'name': 'Sandor', 'age': 50, 'hobbies': ['Drinking', 'Violence']}, 
         {'name': 'Arya', 'age': 19, 'hobbies': ['Sailing', 'Dancing']}]


# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
compre = [person['name'] for person in lista]
print(compre)


# 3) Use a list comprehension to check whether all persons are older than 20.

old_enough = all([person['age'] > 20 for person in lista])
print(old_enough)


# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
backup = lista[:]
print(backup)

# 5) Unpack the persons of the original list into different variables and output these variables.
a, b, c = lista
print(c)
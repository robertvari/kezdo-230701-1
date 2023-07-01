import pprint

phonebook = {
    "06201234567": {"name": "Kiss Csaba", "email": "csaba@gmail.com"},
    "06209876543": {"name": "Nagy Krisztina", "email": "kriszta@gmail.com"},
    "06205448535": {"name": "Kovács Géza", "email": "geza@gmail.com"},
    "06309871234": {"name": "Nagy Csaba", "email": "ncsaba@gmail.com"},
}

# add item to a dictionary
phonebook["06209998877"] = {"name": "Kocsis Balázs", "email": "balazs@gmail.com"}
print(phonebook)

phonebook["06209998877"]["address"] = "Budapest"
print(phonebook["06209998877"])

# update an item in a dictionary
phonebook["06201234567"]["email"] = "kcsaba@gmail.com"
# print(phonebook["06201234567"])

# delete an item from a dictionary
del phonebook["06309871234"]
# print(phonebook)

pprint.pprint(phonebook)
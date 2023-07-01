my_friends = []

# add item to a list
my_friends.append("Csaba")
my_friends.append("Csilla")
my_friends.append("Kriszta")


my_friends.insert(0, "Tamás")
print(my_friends)

# remove items from a list
print(my_friends)
my_friends.remove("Csaba")
print(my_friends)

del my_friends[1]
print(my_friends)

# update an item in a list
my_friends[0] = "Csilla"
print(my_friends)
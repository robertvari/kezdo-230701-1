username = "robert"
password = "testpas123"

input_username = input("What is your username?")
input_password = input("What is your password?")

#           True                             True
if (username == input_username) and (password == input_password):
    print(f"Wellcome {username}. You are logged in.")
else:
    print("username and/or password is invalid.")
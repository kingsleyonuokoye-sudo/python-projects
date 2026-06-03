users = []

file_handle = open("authorized_users.txt", "r")
data = file_handle.readlines()

for d in data:
    tmp = d.strip().split(",")

    user = {}

    user['username'] = tmp[0]
    user['pass'] = tmp[1]
    user['level'] = int(tmp[2])

    users.append(user)

file_handle.close()

username = input("Please enter your username: ")
password = input("Please enter your password: ")

authorized = False

for user in users:
    if username == user['username'] and password == user['pass']:
        authorized = True

if authorized:

    # PASTE YOUR tilling_the_soil.py CODE HERE
    print("Welcome to the Fertilizer Calculator!")

else:
    print("You have entered invalid credentials, please find your password and start over")
    
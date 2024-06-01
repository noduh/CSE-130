# 1. Name:
#      Noah Jorgensen
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This program uses a json file to check username and password combinations
# 4. What was the hardest part? Be as specific as possible.
#      I was unsure of how to get the data into two separate lists. I found the answer on the development forum.
# 5. How long did it take for you to complete the assignment?
#      I think it took about 1.5 hours

import json

# Try to open the json and store to lists
lab02_json_data = None
usernames = []
passwords = []
try:
    lab02_json_file = open("Lab02.json", "r")
    lab02_json_data = json.load(lab02_json_file)
    lab02_json_file.close()
except FileNotFoundError:
    print("Unable to open file Lab02.json")

if lab02_json_data != None:
    usernames = lab02_json_data["username"]
    passwords = lab02_json_data["password"]

    # Check for correct username and password
    username_input = input("Username: ")
    password_input = input("Password: ")
    index_to_check = None
    authenticated = False
    if username_input in usernames:
        index_to_check = usernames.index(username_input)
    if index_to_check != None:
        if password_input == passwords[index_to_check]:
            authenticated = True

    # give the correct response based on correct or incorrect uname/pass
    if authenticated:
        print("You are authenticated!")
    else:
        print("You are not authorized to use the system.")

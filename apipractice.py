import json

print("--- MY USER DATA ---")

try:
    with open("users1.json", "r") as file:
        users = json.load(file)

    for user in users:
        for user in users: 
             print("\nID:", user["id"])
             print("Name:", user["name"])
             print("Department:", user["department"])
             print("College:", user["college"])
             print("Email:", user["email"])
             print("---------------------------")
except FileNotFoundError:
    print("users.json file not found.")
           
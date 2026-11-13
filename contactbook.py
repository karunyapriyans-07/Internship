import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: contacts.json has invalid data.")
            return {}
    else:
        return {}


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not phone.isdigit():
        print("Phone number must contain only numbers.")
        return

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    print("Contact added successfully.")


def search_contact(contacts):
    name = input("Enter name to search: ").strip()

    if name in contacts:
        print("\nContact found")
        print("Name  :", name)
        print("Phone :", contacts[name]["phone"])
        print("Email :", contacts[name]["email"])
    else:
        print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    print("\n--- CONTACTS ---")

    for name, details in contacts.items():
        print("\nName  :", name)
        print("Phone :", details["phone"])
        print("Email :", details["email"])


def main():
    contacts = load_contacts()

    while True:
        print("\n--- CONTACT BOOK ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View Contacts")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_contact(contacts)

            elif choice == 2:
                search_contact(contacts)

            elif choice == 3:
                delete_contact(contacts)

            elif choice == 4:
                view_contacts(contacts)

            elif choice == 5:
                print("Thank you!")
                break

            else:
                print("Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a number.")


main()
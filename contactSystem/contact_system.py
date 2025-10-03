import json
import os
import re

def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    if not is_valid_email(email):
        print("Invalid email format. Please try again.")
        return None

    try:
        age = int(age)
    except ValueError:
        print("Age must be a number.")
        return None

    person = {"name": name, "age": age, "email": email}
    return person

def is_valid_email(email):
    # Simple regex for email validation
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def display_people(people):
    if not people:
        print("No contacts available.")
        return
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])

def delete_contact(people):
    display_people(people)

    while True:
        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range.")
            else:
                break
        except ValueError:
            print("Invalid number. Please enter a valid integer.")

    deleted_person = people.pop(number - 1)
    print(f"Deleted person: {deleted_person['name']}.")

def search(people):
    search_name = input("Search for a name: ").lower()
    results = [person for person in people if search_name in person["name"].lower()]
    
    if results:
        display_people(results)
    else:
        print("No matches found.")

# Load contacts from JSON file, handle errors
if os.path.exists("contacts.json"):
    with open("contacts.json", "r") as f:
        try:
            people = json.load(f).get("contacts", [])
        except json.JSONDecodeError:
            print("Error reading contacts. Starting with an empty list.")
            people = []
else:
    print("Contacts file not found. Starting with an empty list.")
    people = []

print("Hi, welcome to the Contact Management System.")
print()

while True:
    print()
    print("Contact list size:", len(people))
    command = input("You can 'Add', 'Delete', 'Search', 'Display' or 'Q' for quit: ").lower()

    if command == "add":
        person = add_person()
        if person:
            people.append(person)
            print("Person added!")
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search(people)
    elif command == "display":
        display_people(people)
    elif command == "q":
        break
    else:
        print("Invalid command.")

# Save contacts to JSON file
with open("contacts.json", "w") as f:
    json.dump({"contacts": people}, f)

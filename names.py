import os 

PHONEBOOK_FILE = "phonebook.txt"

def load_contacts():
    contacts = {}
    if os.path.exists(PHONEBOOK_FILE):
        with open(PHONEBOOK_FILE, 'r') as file:
            for line in file:
                name, number = line.strip().split(',')
                contacts[name] = number
    return contacts

def save_contacts(contacts):
    with open(PHONEBOOK_FILE, 'w') as file:
        for name, number in contacts.items():
            file.write(f"{name},{number}\n")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
    else:
        for name, number in contacts.items():
            print(f"{name}: {number}")
    print()

def add_contact(contacts):
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    contacts[name] = number
    print(f"Contact '{name}' added.\n")

def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"Contact not found.\n")

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.\n")
    else:
        print(f"Contact not found.\n")

def main():
    contacts = load_contacts()
    
    while True:
        print("\n===== Phone Book Menu =====")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            view_contacts()
        elif choice == '2':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Phonebook saved. Goodbye!")
            break
        else:
            print("Invalid option, please try again.\n")

if __name__ == "__main__":
    main()
        

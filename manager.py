


from file_handling import save_contacts
from helper import search, view, name_input, phone_input, email_input, address_input



def add_contact(contacts):
    name = name_input()
    phone = phone_input(contacts)
    email = email_input()
    address = address_input()
    
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(new_contact)
    view([new_contact], text="New Contact Added")
    save_contacts(contacts, text = "Contact saved successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        view(contacts)


def search_contacts(contacts):
        key = input("Enter search key: ")
        found = search(contacts, key)
        if found:
            view(found, text = "Search Result")
        else:
            print("No contacts found matching the search key.")


def remove_contact(contacts):
    key = input("Enter the name of the contact to remove: ")
    contact_to_remove = next(iter(search(contacts, key)), None)
    if contact_to_remove:
        view([contact_to_remove], text = "Removed contact")
        contacts.remove(contact_to_remove)
        save_contacts(contacts, text = "Contact removed successfully.")
    else:
        print(f"{key} not found.")
        
def remove_all_contacts(contacts):
    confirmation = input("Are you sure you want to remove all contacts? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        contacts.clear()
        save_contacts(contacts, text = "All contacts removed successfully.")
        print("All contacts have been removed.")
    elif confirmation == 'no':
        print("Operation cancelled. No contacts were removed.")
    else:
        print("Invalid input. Operation cancelled. No contacts were removed.")
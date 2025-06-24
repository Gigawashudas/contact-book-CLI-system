from file_handling import save_contacts
from validator import is_valid_phone, is_unique_phone, is_unique_email, is_valid_email


def add_contact(contacts):
    phone = input("Enter contact phone number: ")
    if not is_valid_phone(phone):
        print("Invalid phone number. It must be 11 digits long and start with '01'.")
        add_contact(contacts)
    elif not is_unique_phone(phone, contacts):
        print("This phone number already exists in the contacts.")
        add_contact(contacts)
    else:
        name = input("Enter contact name: ")
        email = input("Enter contact email: ")
        if not is_valid_email(email):
            print("Invalid email format. Please enter a valid email address.")
            add_contact(contacts)
        elif not is_unique_email(email, contacts):
            print("This email already exists in the contacts.")
            add_contact(contacts)
        else:
            address = input("Enter contact address: ")
            contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            print(f"Contact {name} added with phone {phone}, email {email}, and address {address}.")
            save_contacts(contacts)
    
    
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for contact in contacts: print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")



def search_contacts(contacts):
    if not contacts:
        print("Phone book is empty.")
    else:
        key = input("Enter search term: ")
        results = [c for c in contacts if (key.lower() in c['name'].lower() or
                                            key.lower() in c['email'].lower() or
                                            key.lower() in c['phone'].lower() or
                                            key.lower() in c['address'].lower())]
        if not results:
            print("No contacts found matching the search term.")
        else:
            print("Search Results:")
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")


def remove_contact(contacts):
    if not contacts:
        print("Phone book is empty.")
    else:
        name = input("Enter the name of the contact to remove: ")
        contact_to_remove = next((c for c in contacts if c['name'].lower() == name.lower()), None)
        if contact_to_remove:
            contacts.remove(contact_to_remove)
            print(f"Contact {name} removed.")
            save_contacts(contacts)
        else:
            print(f"Contact {name} not found.")
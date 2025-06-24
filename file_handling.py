


import csv




def load_contacts(contact_book='contacts.csv'):
    contacts = []
    try:
        with open(contact_book, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        print("No contacts file found. Starting with an empty phone book.")
    return contacts

def save_contacts(contacts, contact_book='contacts.csv'):
    with open(contact_book, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'phone', 'email', 'address'])
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)
    print("Contacts saved successfully.")

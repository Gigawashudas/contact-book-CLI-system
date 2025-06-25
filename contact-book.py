


from manager import add_contact, view_contacts, remove_contact, search_contacts
from file_handling import load_contacts



contacts = load_contacts('contacts.csv')

while True:
    print("\n=========== MENU ===========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")
    print("============================")

    choice = input("Enter your choice: ")
    
    if choice == '1': add_contact(contacts)
    elif choice == '2': view_contacts(contacts)
    elif choice == '3': search_contacts(contacts)
    elif choice == '4': remove_contact(contacts)
    elif choice == '5': print("Exiting the program. Goodbye!") ; break
    else: print("Invalid choice. Please try again.")
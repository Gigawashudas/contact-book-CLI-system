


from manager import add_contact, view_contacts, remove_contact, search_contacts, remove_all_contacts
from file_handling import load_contacts



contacts = load_contacts('contacts.csv')

while True:
    print("\n=========== MENU ===========")
    print("1. Add Contact     2. View Contacts     3. Search Contacts")
    print("4. Remove Contact  5. Remove All        6. Exit")
    print("============================")

    choice = input("Enter your choice: ")
    
    if choice == '1': add_contact(contacts)
    elif choice == '2': view_contacts(contacts)
    elif choice == '3': search_contacts(contacts)
    elif choice == '4': remove_contact(contacts)
    elif choice == '5': remove_all_contacts(contacts)
    elif choice == '6': print("Exiting the program. Goodbye!") ; break
    else: print("Invalid choice. Please try again.")
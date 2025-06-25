


from validator import is_valid_phone, is_unique_phone, is_valid_email


def search(contacts, key):
    if not contacts:
        print("Phone book is empty.")
    else:
        results = [c for c in contacts if (key.lower() in c['name'].lower() or
                                            key.lower() in c['email'].lower() or
                                            key.lower() in c['phone'].lower() or
                                            key.lower() in c['address'].lower())]
        if not results:
            return False
        else:
            return results


def view(contacts, text='Contacts'):
    if not contacts:
        print("No contacts found.")
    else:
        print(f"\n{text}:\n--------------------")
        for contact in contacts:
            print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n--------------------")


def name_input():
    
    while True:
        fname = str(input("Enter your first name: ").strip())
        if not fname:
            print("First name cannot be empty. Please enter a valid name.")
        elif not fname.isalpha():
            print("First name must contain only alphabetic characters. Please enter a valid name.")
        else:
            break
    
    while True:
        lname = str(input("Enter your last name: ").strip())
        if not lname:
            print("Last name cannot be empty. Please enter a valid name.")
        elif not lname.isalpha():
            print("Last name must contain only alphabetic characters. Please enter a valid name.")
        else:
            break
    return f"{fname} {lname}"


def phone_input(contacts):
    while True:
        phone = input("Enter contact phone number: ").strip()
        if not is_valid_phone(phone):
            print("Invalid phone number. It must be 11 digits long and start with '01'.")
        elif not is_unique_phone(phone, contacts):
            print("This phone number already exists in the contacts.")
        else:
            break
    return phone


def email_input():
    while True:
        email = input("Enter contact email: ").strip()
        if not is_valid_email(email):
            print("Invalid email format. Please enter a valid email address.")
        else:
            break
    return email


def address_input():
    while True:
        address = input("Enter contact address: ").strip()
        if not address:
            print("Address cannot be empty. Please enter a valid address.")
        else:
            break
    return address
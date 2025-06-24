




def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 11 and phone.startswith("01")


def is_unique_phone(phone, contacts):
    for contact in contacts:
        if contact['phone'] == phone:
            return False
    return True


def is_unique_email(email, contacts):
    for contact in contacts:
        if contact['email'].lower() == email.lower():
            return False
    return True


def is_valid_email(email):
    return "@" in email and "." in email and email.index("@") < email.rindex(".")

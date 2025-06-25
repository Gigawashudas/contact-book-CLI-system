


def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 11 and phone.startswith("01") and phone[2] in "356789"


def is_unique_phone(phone, contacts):
    return not any(contact['phone'] == phone for contact in contacts)


def is_valid_email(email):
    return "@" in email and "." in email and email.index("@") < email.rindex(".") and email.index("@") > 0 and email.rindex(".") < len(email) - 1 and email.index("@") < len(email) - 1 and email.index(".") > 0 and email.index(".") < len(email) - 1

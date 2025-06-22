#contact.py
#This module defines a Contact class
class Contact:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        
    def __str__(self):
        return (f"name: {self.name}, "
                f"email: {self.email}, "
                f"phone: {self.phone}, "
                f"address: {self.address}")
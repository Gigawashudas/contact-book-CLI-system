


To start the project run main.py


# contact book CLI system

TASKS:

Add Contacts:

-Allow users to add contacts with at least the following details: Name, Email, Phone

Number, and Address.

-You can include additional fields if necessary.

Prevent Duplicate Numbers:

-Ensure that the same phone number cannot be assigned to multiple names.

View Contacts:

- Display all saved contacts in a well-organized format. A neat and user-friendly presentation is encouraged.

Save to File

- Store all contact information in a file of your choice (example .txt, .csv, .json etc.).

- Contacts should be automatically saved to the file upon addition.

Load from File:

- Ensure all previously saved contact data is loaded when the program starts.

Remove Contacts:

- Provide an option to delete contacts from the file.

BONUS FEATURES:

Search Contacts:

-Implement functionality to search for specific contacts based on their details.

Error Handling:

Display meaningful error messages for invalid inputs, such as:

~~The contact's name must be a string.

~~The phone number must be an integer.

~~Provide clear guidance to users on resolving input issues.

NOTES:

File Structure:

Organize your project into multiple Python files, each dedicated to specific features or functionalities.

Modular Code:

-Write reusable and maintainable code by encapsulating features within functions.

No External Libraries:

-Use only the Python as taught in the course. Avoid third-party packages or frameworks.

Menu System:

-Design an interactive menu with an Exit option for easy navigation. All features should be

accessible from this menu.

Sample Input/Output:

Sample 1: Program Startup (Loading Contacts)

Welcome to the Contact Book CLI System!

Loading contacts from contacts.csv... Done!

=========== MENU ==

1. Add Contact

2. View Contacts

3. Search Contact

4. Remove Contact

5. Exit

==

Enter your choice: 2

===== All Contacts =====

1. Name : Alice Smith

Phone : 01711223344

Email: alice@example.com

Address: 12/A Lake View, Dhaka

2. Name : Bob Rahman

Phone : 01812345678

Email: bob@example.com

Address: 7 Green Street, Chittagong

==

Sample 2: Add Contact (Successful Entry)

=========== MENU ==

1. Add Contact

2. View Contacts

3. Search Contact

4. Remove Contact

5. Exit

==

Enter your choice: 1

Enter Name: John Doe

Enter Phone Number: 01911223344

Enter Email: john@example.com

Enter Address: 15/B Road 10, Sylhet

Contact added successfully!

Sample 3: Add Contact (Duplicate Phone Number)

Enter Name: Junaid Khan

Enter Phone Number: 01911223344

Enter Email: junaid@example.com

Enter Address: 55 Gulshan, Dhaka

Error: Phone number already exists for another contact.

Sample 4: Search Contact (Partial Name)

Enter search term (name/email/phone): alice

Search Result:

Name : Alice Smith

Phone : 01711223344

Email: alice@example.com

Address: 12/A Lake View, Dhaka

Sample 5: Remove Contact (By Phone Number)

Enter the phone number of the contact to delete: 01711223344

Are you sure you want to delete contact numbers 01711223344? (y/n): y

Contact deleted successfully!

Sample 6: Exit

Thank you for using the Contact Book CLI System. Goodbye!
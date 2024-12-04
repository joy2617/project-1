

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, details in contacts.items():
            phone = details['number']
            email = details['Email']
            address = details['address']
            print(f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}")
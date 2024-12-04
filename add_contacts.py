from all_save import save_all

def add_contact(contacts):
    name = input("Enter contact name: ")
    if not name.isalpha():
        print("The contact name must be a string.")
        return contacts
         
    phone = input("Enter contact phone number: ")
    if not phone.isdigit():
        print("The contact number must be a integer.")
        return contacts
             
    email = input("Enter your Email: ")
    address = input("Enter your address: ")
     
     
      #To Prevent Duplicate Numbers

    for contact in contacts.values():
        if contact['number'] == phone:
            print("This phone number is already added.")
            return contacts

    
    contact = {
        "number": phone,
        "Email": email,
        "address": address
    }
    
    
    contacts[name] = contact
    save_all(contacts)
         
    
    
    print("Contact added successfully")
    
    return contacts

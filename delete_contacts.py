
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    phone= input("Enter phone number: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{phone}' deleted successfully!")
        
    else:
        print("Contact not found.")

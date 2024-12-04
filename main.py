import add_contacts
import view_contact
import delete_contacts



contacts = {}

def display_menu():
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Search Contact")    
    print("5. Exit")


  # To Find Contacts
def search_contacts():
    search_term = input("Enter the name, phone number, email, or address to search: ").lower()
    
    results = {name: details for name, details in contacts.items() if search_term in name.lower() or search_term in details['number'].lower() or search_term in details['Email'].lower() or search_term in details['address'].lower()}

    if not results:
        print("No matching contacts found.")
    else:
        for name, details in results.items():
            phone = details['number']
            email = details['Email']
            address = details['address']
            print("Matching contacts found.....")
            print(f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}")



def main():
    while True:
        display_menu()
    
        choice = input("Choose an option: ")

        if choice == '1':
            add_contacts.add_contact(contacts)
        elif choice == '2':
            view_contact.view_contacts(contacts)
            
        elif choice == '3':
            delete_contacts.delete_contact(contacts)

        elif choice == '4':
            search_contacts()    
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()

import json

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email, address):
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        self.save_contacts()
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available!")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact['name']} - {contact['phone']}")

    def search_contact(self, keyword):
        results = [contact for contact in self.contacts if keyword.lower() in contact['name'].lower() or keyword in contact['phone']]
        if results:
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        else:
            print("No contact found!")

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                if new_phone:
                    contact['phone'] = new_phone
                if new_email:
                    contact['email'] = new_email
                if new_address:
                    contact['address'] = new_address
                self.save_contacts()
                print("Contact updated successfully!")
                return
        print("Contact not found!")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                print("Contact deleted successfully!")
                return
        print("Contact not found!")

def main():
    book = ContactBook()
    while True:
        print("\nContact Book Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            book.add_contact(name, phone, email, address)
        elif choice == "2":
            book.view_contacts()
        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            book.search_contact(keyword)
        elif choice == "4":
            name = input("Enter name of the contact to update: ")
            new_phone = input("Enter new phone number (press enter to skip): ")
            new_email = input("Enter new email (press enter to skip): ")
            new_address = input("Enter new address (press enter to skip): ")
            book.update_contact(name, new_phone or None, new_email or None, new_address or None)
        elif choice == "5":
            name = input("Enter name of the contact to delete: ")
            book.delete_contact(name)
        elif choice == "6":
            print("Exiting application...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

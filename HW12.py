import pickle

class Field:
    def __init__(self, value=None):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    pass


class Phone(Field):
    @Field.value.setter
    def value(self, value):
        if isinstance(value, str) and value.isdigit():
            self._value = value
        else:
            print('The phone number must contain only digits.')


class BirthDate(Field):
    pass


class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, birthdate):
        self.contacts[name] = {'phone': phone, 'birthdate': birthdate}

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def search_contacts(self, query):
        matching_contacts = []
        for name, contact in self.contacts.items():
            if query.lower() in name.lower() or query.lower() in contact['phone'].lower() or query.lower() in contact['birthdate'].lower():
                matching_contacts.append((name, contact['phone'], contact['birthdate']))
        return matching_contacts

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.contacts, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            print("File not found. Empty address book loaded.")

    def display_contacts(self):
        if not self.contacts:
            return "No contacts found."
        else:
            output = ""
            for name, contact in self.contacts.items():
                output += f"Name: {name}, Phone: {contact['phone']}, Birthdate: {contact['birthdate']}\n"
            return output.strip()


def main():
    address_book = AddressBook()

    while True:
        print("1. Add contact")
        print("2. Remove contact")
        print("3. Search contacts")
        print("4. Save address book")
        print("5. Load address book")
        print("6. Display contacts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            birthdate = input("Enter birthdate: ")
            address_book.add_contact(name, phone, birthdate)
            print("Contact added successfully.")
        elif choice == "2":
            name = input("Enter name to remove: ")
            address_book.remove_contact(name)
            print("Contact removed successfully.")
        elif choice == "3":
            query = input("Enter search query: ")
            results = address_book.search_contacts(query)
            if results:
                print("Matching contacts:")
                for name, phone, birthdate in results:
                    print(f"Name: {name}, Phone: {phone}, Birthdate: {birthdate}")
            else:
                print("No matching contacts found.")
        elif choice == "4":
            filename = input("Enter filename to save: ")
            address_book.save_to_file(filename)
            print("Address book saved successfully.")
        elif choice == "5":
            filename = input("Enter filename to load: ")
            address_book.load_from_file(filename)
            print("Address book loaded successfully.")
        elif choice == "6":
            contacts = address_book.display_contacts()
            print(contacts)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

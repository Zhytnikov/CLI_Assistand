from collections import UserDict

# батьківський клас Field
class Field:
    def __init__(self, value): #
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field): 
    pass  

class Phone(Field):  
    def __init__(self, value):
        super().__init__(value)
        self.validate_phone()

    def validate_phone(self):
        if not self.value.isdigit() or len(self.value) != 10:
            raise ValueError("Invalid phone number format. Please enter a 10 digit phone number.")

class Record: 
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                break

    def edit_phone(self, old_phone_number, new_phone_number):
        phone_exists = False
        for phone in self.phones:
            if phone.value == old_phone_number:
                phone.value = new_phone_number
                phone_exists = True
                break

        if not phone_exists:
            raise ValueError("Phone number to edit does not exist in the contact's phone list")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        phone_list = "; ".join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name}, phones: {phone_list}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]



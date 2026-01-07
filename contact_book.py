

from file_manager import FileManager
from contact import Contact

class ContactBook:
   def __init__(self):
      self.contacts = FileManager.load_contacts()

   def add_contact(self, name, phone, email):
      self.contacts.append(Contact(name, phone, email))
      FileManager.save_contacts(self.contacts)

   def view_contacts(self):
      return self.contacts
   
   def search_contact(self, name):
      for contact in self.contacts:
         if contact.name.lower() == name.lower():
            return contact
      return None
   
   def delete_contact(self, name):
      self.contacts = [c for c in self.contacts if c.name.lower() != name.lower()]
      FileManager.save_contacts(self.contacts)

      
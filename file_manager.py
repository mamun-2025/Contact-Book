
import os
from contact import Contact

class FileManager:
   BASE_DIR = os.path.dirname(os.path.abspath(__file__))
   FILE_PATH = os.path.join(BASE_DIR, "contacts.txt")

   @staticmethod
   def save_contacts(contacts):
      with open(FileManager.FILE_PATH, "w") as file:
         for contact in contacts:
            file.write(contact.to_string() + "\n")

   @staticmethod
   def load_contacts():
      Contacts = []
      try: 
         with open(FileManager.FILE_PATH, "r") as file:
            for line in file:
               name, phone, email = line.strip().split("|")
               Contacts.append(Contact(name, phone, email))
      except FileNotFoundError:
         pass
      return Contacts



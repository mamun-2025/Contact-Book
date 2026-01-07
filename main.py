

from contact_book import ContactBook

app = ContactBook()

while True:
   print("\n1. Add Contact")
   print("2. View Contacts")
   print("3. Search Contact")
   print("4. Delete Contact")
   print("5. Exit")

   choice = input("Choose an Option: ")

   if choice == "1":
      app.add_contact(
         input("Name: "),
         input("Phone: "),
         input("Email: ")
      )
      print("Contact added successfully!")
   elif choice == "2":
      print("---Contact List---")
      for c in app.view_contacts():
         print(c.to_string())
   
   elif choice == "3":
      name = input("Enter name: ")
      result = app.search_contact(name)
      print("---Found---")
      print(result.to_string() if result else "Contact not found")

   elif choice == "4":
      app.delete_contact(input("Enter name: "))

   elif choice == "5":
      break

   else:
      print("Invalid Option")
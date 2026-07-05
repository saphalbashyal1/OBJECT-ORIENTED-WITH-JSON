import json
import os

class Contact:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
    
    def show_details(self):
        return(
            f"Name = {self.name}\n"
            f"Phone = {self.phone}\n"
            f"Email = {self.email}"
        )
    
    def to_dict(self):
        return{
            "name":self.name,
            "phone":self.phone,
            "email":self.email
        }
    
    def set_phone(self,newphone):
        self.phone=newphone

class contactBook:
    def __init__(self):
        self.contacts={}
        self.file="contacts.json"
        self.load_contacts()
    
    def load_contacts(self):
        if not os.path.exists(self.file):
            return
        with open(self.file,"r") as f:
            data = json.load(f)
            for name , details in data.items():
                self.contacts[name]=Contact(details["name"],details["phone"],details["email"])
    
    def save_contacts(self):
        with open(self.file,"w") as f:
            data={}
            for name,contact in self.contacts.items():
                data[name]=contact.to_dict()
            json.dump(data,f,indent=4)
    
    def add_contacts(self):
        name=input("Enter Name: ")
        if name in self.contacts:
            print("User already exists!!")
            return
        phone=input("Enter Phone: ")
        if not phone.isdigit() or len(phone) != 10:
            print("Invalid phone — must be 10 digits")
            return
        email=input("Enter Email: ")
        objec=Contact(name,phone,email)
        self.contacts[name]=objec
        self.save_contacts()
        print("Contact Successfully Added!!")
    
    def show_contact(self):
        if not self.contacts:
            print("Empty one!!")
            return
        name=input("Enter Name: ")
        if name not in self.contacts:
            print('name not found!!')
            return
        object1=self.contacts[name] 
        print(object1.show_details()) 
    
    def update_phone(self):
        name=input("Enter Name: ")
        if name not in self.contacts:
            print("Name not found!!")
            return  
        newphone = input("Enter New phone: ")
        if not newphone.isdigit() or len(newphone) != 10:
            print("Invalid phone — must be 10 digits")
            return
        object2=self.contacts[name]      
        object2.set_phone(newphone)
        self.save_contacts()
        print("Updated Successfully!!")
    
    def delete_contact(self):
        name=input("Enter Name: ")
        if name not in self.contacts:
            print("Name not found!!")
            return
        confirm=input("Do you really want to delete??(yes/no)").lower()
        if confirm=="yes" or confirm=="y":
            del(self.contacts[name])
            self.save_contacts()
            print("---Deleted Successfully---")
            return
    
    def show_all_contacts(self):
        if not self.contacts:
            print("Empty one!!")
            return
        for name in self.contacts.values():
            print(name.show_details())
        print(f"Total contacts is : {len(self.contacts)}")
        
              
manager=contactBook()
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Show Contact")
    print("3. Update Phone")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Exit")
    choice = int(input("Enter choice [1-6]: "))   
    if choice == 1:
        manager.add_contacts()
    elif choice == 2:
        manager.show_contact()
    elif choice == 3:
        manager.update_phone()
    elif choice == 4:
        manager.delete_contact()
    elif choice == 5:
        manager.show_all_contacts()
    elif choice == 6:
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
               
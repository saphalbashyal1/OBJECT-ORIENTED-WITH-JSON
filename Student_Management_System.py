import json
import os

class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
        
    def show_details(self):
        return(
            f"Name:{self.name}\n"
            f"Age:{self.age}\n"
            f"Grade:{self.grade}"
        )
        
    def to_dict(self):
        return{
            "name":self.name,
            "age":self.age,
            "grade":self.grade
        
        }
        
    def set_grade(self,newgrade):
        self.grade=newgrade
        
class StudentManager:
    def __init__(self):
        self.students={}
        self.file="Student.json"
        self.load_student()
    
    def load_student(self):
        if not os.path.exists(self.file):
            return
        
        with open(self.file,"r") as f:
            data=json.load(f)
            for name,details in data.items():
                self.students[name]=Student(details["name"],details["age"],details["grade"])
     
    def save_student(self):
        with open(self.file,"w") as f:
            data={}
            for name,student in self.students.items():
                data[name]=student.to_dict()
            json.dump(data,f,indent=4)
                     
    def add_student(self):
        name=input("Enter Name: ")
        if name in self.students:
            print("Student already exists.")
            return
        age=int(input("Enter Age: "))
        try:
            grade = int(input("Enter Grade: "))
        except ValueError:
            print("Grade must be a number")
            return

        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100")
            return
        
        student=Student(name,age,grade)
        self.students[name]=student
        self.save_student()
        print(f"Student Name {name} added successfully!!")
    
    def show_student(self):
        if not self.students:
            print("Empty one!!")
            return
        
        name=input("Enter Name: ")
        if name not in self.students:
            print("Name doesn't exists")
            return
        objec=self.students[name]
        print(objec.show_details())
        
    def upgrade_grade(self):
        name=input("Enter Name: ")
        if name not in self.students:
            print("name doesn't exists.")
            return
        try:
            new_grade = int(input("Enter Grade: "))
        except ValueError:
            print("Grade must be a number")
            return

        if new_grade < 0 or new_grade > 100:
            print("Grade must be between 0 and 100")
            return
        
        objec2=self.students[name]
        objec2.set_grade(new_grade)
        self.save_student()
        print(f"Grade updated successfully to {new_grade}")
        
    def delete_student(self):
        name=input("Enter Name: ")
        if name not in self.students:
            print("Name doesn't exists.")
            return
        confirm=input("Do you really want to delete the name?? (yes/no)").lower()
        if confirm=="yes" or confirm=="y":
            del(self.students[name])
            self.save_student()
            print("Deleted Successfully!!")
            return
        
    def show_all_students(self):
        if not self.students:
            print("Empty Record!!")
            return
        for user in self.students.values():
            print("=====================")
            print(user.show_details())
        print("=====================")
        print(f"Total students is {len(self.students)}")
        
    def show_topper(self):
        if not self.students:
            print("Empty Record!!")
            return
        topper=None
        for student in self.students.values():
            if topper is None or student.grade>topper.grade:
                topper=student
            self.save_student()
        print(f"The topper is \n {topper.show_details()}")
               
manager=StudentManager()
 
while True:
    print("1.Add_student")
    print("2.show_student")
    print("3.update_grade")
    print("4.delete_student")
    print("5.Show all student")
    print("6.Show topper ")
    print("7.Exit")
    try:
        choice=int(input("Enter your choice[1-7]: "))
    except ValueError:
        print("please enter a valid number between 1 and 7.")
        continue
    if choice==1:
        manager.add_student()
        continue    
    elif choice==2:
        manager.show_student()
        continue
    elif choice==3:
        manager.upgrade_grade()
        continue
    elif choice==4:
        manager.delete_student()
        continue
    elif choice==5:
        manager.show_all_students()
        continue
    elif choice==6:
        manager.show_topper()
        continue
    elif choice==7:
        print("Exitted Successfully!!")
        break
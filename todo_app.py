import json
import os

class task:
    def __init__(self,title,status="pending"):
        self.title=title
        self.status=status
        
    def show_details(self):
        return(
            f"Title: {self.title}\n"
            f"Status:{self.status}"
        )
        
    def to_dict(self):
        return{
            "title":self.title,
            "status":self.status,
        }
        
class Todo_App:
    def __init__(self):
        self.tasks={}
        self.file="tasks.json"
        self.load_tasks()
    
    def load_tasks(self):
        if not os.path.exists(self.file):
            return
        with open(self.file,"r") as f:
            data=json.load(f)
            for title,detail in data.items():
                self.tasks[title]=task(detail["title"],detail["status"])
    
    def save_tasks(self):
        with open(self.file,"w") as f:
            data={}
            for name,detail in self.tasks.items():
                data[name]=detail.to_dict()               
            json.dump(data,f,indent=4)
    
    def add_task(self):
        title = input("Enter title: ")
        if title in self.tasks: 
            print("Task already exists!!")
            return
        Task = task(title)
        self.tasks[title] = Task
        self.save_tasks()
        print("Task Successfully Added!!")
    
    def mark_complete(self):
        title=input("Enter title: ")
        if title not in self.tasks:
            print("Task not found!!")
            return
        current_task = self.tasks[title]
        if current_task.status == "completed":
            print("Task already completed.")
            return
        current_task.status = "completed"
        self.save_tasks()
        print(f"task {title} marked as completed.")
    
    def show_all_tasks(self):
        if not self.tasks:
            print("Sorry!!")
            return
        
        for value in self.tasks.values():
            print(value.show_details())
        print(f"Total count: {len(self.tasks)}") 
    
    def show_pending(self):
        if not self.tasks:
            print("Empty one!!")
            return
        print("Pending tasks!!")
        found=False
        for task in self.tasks.values():
            if task.status == "pending":
                print(task.show_details())
                found=True
        if not found:
            print("No compeleted tasks!!")
    
    def show_completed(self):
        if not self.tasks:
            print("Empty one!!")
            return
        print("========Completed Task!!========")
        found=False
        for task in self.tasks.values():
            if task.status=="completed":
                print(task.show_details())
                found=True
        if not found:
            print("No completed tasks!!")
         
    def delete_task(self):
        if not self.tasks:
            print("Empty file!")
            return
        title=input("Enter title: ")
        if title not in self.tasks:
            print("Task not found.")
            return
        choice=input("Do you really want to delete??(yes/no)").lower().strip()
        if choice=="yes" or choice=="y":
            del(self.tasks[title])
            self.save_tasks()
            print("Deleted Successfully!!")
            return
        
manager=Todo_App()
while True:
    print("1.Add Task")       
    print("2.Mark Complete")     
    print("3.Show All Tasks")
    print("4.Show Pending") 
    print("5.Show Completed")  
    print("6.Delete Task")  
    print("7.Exit")
    try:
        choice=int(input("Enter choice: "))
        if choice==1:
            manager.add_task()
            continue
        elif choice==2:
            manager.mark_complete()
            continue
        elif choice==3:
            manager.show_all_tasks()
            continue
        elif choice==4:
            manager.show_pending()
            continue
        elif choice==5:
            manager.show_completed()
            continue
        elif choice==6:
            manager.delete_task()
            continue
        elif choice==7:
            print("Successfully Exitted!!")
            break
    except ValueError:
        print("please input number between [1-7]!!")
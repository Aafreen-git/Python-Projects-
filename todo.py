import json


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = {"title": title, "done": False}
        self.tasks.append(task)
        print(f" '{title}' added!")


    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks yet!")
            return
        for index, task in enumerate(self.tasks, 1):
            status = "X" if task ["done"] else ""
            print(f"{index}. [{status}] {task['title']}")
        
    def complete_task(self,index):
        self.tasks[index - 1]["done"] = True
        print(f"Task Completed!")
    
    def delete_task(self, index):
        removed = self.tasks.pop(index - 1)
        print(f" '{removed['title']}' deleted!")

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
        print(" Tasks saved!")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = [] 

def main():
    todo = ToDoList()
    todo.load_tasks()

    while True:
        print("\n==== TO DO LIST ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            title = input("enter task: ")
            todo.add_task(title)
            todo.save_tasks()
        elif choice == "2":
            todo.view_tasks()
        elif choice =="3":
            todo.view_tasks()
            index = int(input("Complete which task? "))
            todo.complete_task(index)
            todo.save_tasks()
        elif choice == "4":
            todo.view_tasks()
            index = int(input("Delete which task? "))
            todo.delete_task(index)
            todo.save_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main()
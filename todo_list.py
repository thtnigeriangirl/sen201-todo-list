tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(i, task)

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("Enter task number to delete: "))
            tasks.pop(task_number - 1)
            print("Task deleted successfully.")
        except:
            print("Invalid input.")

def main_menu():
    while True:
        print("\nTO-DO LIST APPLICATION")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting application.")
            break
        else:
            print("Invalid choice.")

main_menu()

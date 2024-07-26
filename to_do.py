tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

def delete_task(task_index):
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task index.")
    else:
        del tasks[task_index]
        print("Task deleted.")

def display_tasks():
    if not tasks:
        print("No tasks.")
    else:
        print("Task List:")
        for index, task in enumerate(tasks):
            status = "✓" if task["completed"] else " "
            print(f"{index + 1}. [{status}] {task['task']}")

def complete_task(task_index):
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task index.")
    else:
        tasks[task_index]["completed"] = True
        print("Task marked as complete.")

def main():
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task to add: ")
            add_task(task)
        elif choice == '2':
            if tasks:
                display_tasks()
                task_index = int(input("Enter task number to delete: ")) - 1
                delete_task(task_index)
            else:
                print("No tasks to delete.")
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            if tasks:
                display_tasks()
                task_index = int(input("Enter task number to mark as complete: ")) - 1
                complete_task(task_index)
            else:
                print("No tasks to mark as complete.")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()

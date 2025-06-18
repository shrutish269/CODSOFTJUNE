# to_do_list.py
def show_menu():
    print("\n----- TO-DO LIST MENU -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")


def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(" Task added!")


def view_tasks(tasks):
    if not tasks:
        print(" No tasks found.")
    else:
        print("\n Your Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")


def update_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the new task description: ")
            tasks[task_num - 1] = new_task
            print(" Task updated!")
        else:
            print(" Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f" Task '{removed}' deleted!")
        else:
            print(" Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting... Have a productive day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")


if __name__ == "__main__":
    main()

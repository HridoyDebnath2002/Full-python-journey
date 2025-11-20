todo_list = []


def show_menu():
    print("\n===== TO-DO APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter your task: ")
        todo_list.append(task)
        print("Task added!")

    # View Tasks
    elif choice == "2":
        if len(todo_list) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")

    # Remove Task
    elif choice == "3":
        if len(todo_list) == 0:
            print("No tasks to remove.")
        else:
            print("Enter task number to remove:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")

            try:
                num = int(input("Task number: "))
                if 1 <= num <= len(todo_list):
                    removed = todo_list.pop(num - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number!")
            except:
                print("Please enter a valid number.")

    # Exit
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")

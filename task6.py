# ---------------------------------------------
# Basic To-Do List Application
# Author: [Your Name]
# Description:
# This program allows the user to add, view, and remove tasks 
# from a to-do list using Python lists.
# ---------------------------------------------

todo_list = []

while True:
    print("\n--- 📝 TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task to add: ")
        todo_list.append(task)
        print(f"✅ '{task}' added to your to-do list.")

    elif choice == '2':
        if not todo_list:
            print("🗒️ Your to-do list is empty.")
        else:
            print("\n📋 Your To-Do List:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")

    elif choice == '3':
        if not todo_list:
            print("⚠️ Nothing to remove — your list is empty!")
        else:
            print("\n📋 Your To-Do List:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the number of the task to remove: "))
                removed = todo_list.pop(task_num - 1)
                print(f"🗑️ '{removed}' removed from the list.")
            except (ValueError, IndexError):
                print("❌ Invalid task number!")

    elif choice == '4':
        print("👋 Exiting the To-Do List. Goodbye!")
        break

    else:
        print("❌ Invalid choice! Please enter a number between 1 and 4.")

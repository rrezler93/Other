# Simple To-Do List Application with File Storage

# Initialize the to-do list
todo_list = []

# Function to save the to-do list to a file
def save_to_file():
    with open("todo_list.txt", "w") as file:
        for task in todo_list:
            file.write(f"{task['task']},{task['done']}\n")

# Function to load the to-do list from a file
def load_from_file():
    try:
        with open("todo_list.txt", "r") as file:
            for line in file:
                task_data = line.strip().split(',')
                task = {"task": task_data[0], "done": task_data[1].strip().lower() == 'true'}
                todo_list.append(task)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        pass


# Load the to-do list from the file at startup
load_from_file()

# Main program loop
while True:
    # Display the menu
    print("\nMenu:")
    print("1. Add a task")
    print("2. Display the to-do list")
    print("3. Mark a task as done")
    print("4. Reset the to-do list")
    print("5. Exit the program")

    # Choose an option
    choice = input("Choose an option: ")

    if choice == "1":
        # Add a task to the list
        task = input("Enter a new task: ")
        todo_list.append({"task": task, "done": False})
        print("Task added!")
        save_to_file()

    elif choice == "2":
        # Display the to-do list
        print("\nTo-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "Done" if task["done"] else "To-Do"
            print(f"{index}. {task['task']} ({status})")

    elif choice == "3":
        # Mark a task as done
        task_number = int(input("Enter the task number to mark as done: "))
        if 1 <= task_number <= len(todo_list):
            todo_list[task_number - 1]["done"] = True
            print("Task marked as done!")
            save_to_file()
        else:
            print("Invalid task number.")

    elif choice == "4":
        # Reset the to-do list (clear the file and the list)
        todo_list = []
        with open("todo_list.txt", "w") as file:
            pass  # Clear the file
        print("To-Do list reset!")

    elif choice == "5":
        # Exit the program
        print("Thank you for using the program!")
        break

    else:
        print("Invalid option. Please choose again.")

# to do.py

# Function to create a new task
def create_task(task_list, task):
    task_list.append(task)

# Function to update an existing task
def update_task(task_list, index, new_task):
    task_list[index] = new_task

# Function to delete a task
def delete_task(task_list, index):
    del task_list[index]

# Function to list all tasks
def list_tasks(task_list):
    if not task_list:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(task_list):
            print(f"{i+1}. {task}")

# Main function
def main():
    tasks = []

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            create_task(tasks, task)
        elif choice == "2":
            index = int(input("Enter the index of the task to update: ")) - 1
            new_task = input("Enter the new task: ")
            update_task(tasks, index, new_task)
        elif choice == "3":
            index = int(input("Enter the index of the task to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == "4":
            list_tasks(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

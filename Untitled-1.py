def menu():
    print("Enter 1 to view all tasks")
    print("Enter 2 to add new task")
    print("Enter 3 to Edit task")
    print("Enter 4 to Search task")
    print("Enter 5 to save tasks")
    print("Enter 6 to Mark task don")
    print("Enter 7 to Remove task")
    print("Enter 8 to Exit")
    try:
        choice=int(input("Enter your choice:"))
        return choice
    except ValueError:
        print("Invalid input")

def read_data():
    with open("to do.txt","r") as f:
        data=f.readlines()
        return data

def write_data(data):
    with open("to do.txt","w") as f:
        f.writelines(data)

def add_data(data):
    with open("to do.txt","a") as f:
        f.write("\n"+data)

def view_task():
    data=read_data()
    if not data:
        print("no tasks avalable")
    else:
        for i, task in enumerate(data):
            print(f"{i+1}. {task.strip()}")

def add_task():
    task = input("Enter new task: ").strip()
    old_data = read_data()
    if task in [i.strip() for i in old_data]:
        print("Task already exists")
        return
    if not old_data:
        write_data([task])
    else:
        add_data(task)
    print("Task added")

def edit_task():
    view_task()
    try:
        num = int(input("Enter task number: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    index = num-1
    data=read_data()
    if 0 <= index < len(data):
        new_task = input("Enter new task: ")
        if new_task in [task.strip() for task in data]:
            print("Task already exists.")
            return
        data[index] = new_task.strip() + "\n"
        write_data(data)
        print("Task updated successfully.")
    else:
        print("Invalid task number.")
        print("Enter 1 to view all tasks")

def search_task():
    data = read_data()
    task = input("Enter the task to search: ").strip()
    found = False
    for i in range(len(data)):
        if task.lower() == data[i].strip().lower():
            print(f"Task found at position {i+1}")
            found = True
            break

    if not found:
        print("Task not found.")

def save_task():
    print("task is saved")
    print("Enter 8 to exit")
    return

def mark_done():
    view_task()
    num = int(input("Enter task number: "))
    data=read_data()
    index = num - 1
    if 0 <= index < len(data):
        if "(Done)" not in data[index]:
            data[index] = data[index].strip() + " (Done)\n"
            write_data(data)
            print("Task marked as done.")
        else:
            print("Task is already marked as done.")
    else:
        print("Invalid task number.")

def remove_task():
    view_task()
    num=int(input("Enter the task number to remove:"))
    data=read_data()
    if 1 <= num <= len(data):
        index=num-1
        data.pop(index)
        write_data(data)
        print("Task removed")
    else:
        print("Invalid Task Number")

while True:
    match menu():
        case 1:
            view_task()
        case 2:
            add_task()
        case 3:
            edit_task()
        case 4:
            search_task()
        case 5:
            save_task()
        case 6:
            mark_done()
        case 7:
            remove_task()
        case 8:
            break
        case _:
            print("invalid choice")
            print("Enter a valid choice")
        

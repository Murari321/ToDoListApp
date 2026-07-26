def menu():
    print("Enter 1 to view all tasks")
    print("Enter 2 to add new task")
    print("Enter 3 to Edit task")
    print("Enter 4 to Search task")
    print("Enter 5 to save tasks")
    print("Enter 6 to Mark task don")
    print("Enter 7 to Remove task")
    print("Enter 8 to Exit")
    choice=int(input("Enter your choice:"))
    return choice
def view_task():
    f=open("to do.txt","r")
    data=f.read()
    print(data)
    f.close()
    return
def add_task():
    f=open("to do.txt","a")
    task=input("Enter the task to be added:")
    f.write("\n"+task)
    f.close()
    print("Task is added")
    return
def edit_task():
    f=open("to do.txt","r")
    data=f.read()
    f.close()
    task=input("entere the task to Edit:")
    if(data.find(task)!=-1):
        new_task=input("Enter the new task:")
        new_data=data.replace(task,new_task)
        print("Task is edited")
        print("Enter the 1 to view all tasks")
        f=open("to do.txt","w")
        f.write(new_data)
        f.close()
    else:
        print("task dosn't exist")
        print("Enter 1 to view all tasks")
    return
def Search_task():
    f=open("to do.txt","r")
    data=f.read()
    task=input("Enter the task to search:")
    if(data.find(task)!=1):
        print("Task is present")
        print("Enter 1 if you want to view the lisk of tasks:")
    else:
        print("tast is not present")
        print("Enter 1 to view all tasks")
    f.close()
    return
def save_task():
    print("task is saved")
    print("Enter 8 to exit")
    return
def mark_done():
    f = open("to do.txt", "r")
    data = f.readlines()
    f.close()

    task = input("Enter task that is done: ")

    for i in range(len(data)):
        if task in data[i]:
            data[i] = data[i].replace(task, task + " (Done)")

    f = open("to do.txt", "w")
    f.writelines(data)
    f.close()
    print("Done")
    return
def remove_task():
    print("Enter the task to remove")
    task=input()
    f=open("to do.txt","r")
    data=f.readlines()
    f.close()

    for i in range(len(data)):
        if task in data[i]:
            data[i]=data[i].replace(task,"")
            print("Task removed")
    f=open("to do.txt","w")
    f.writelines(data)
    f.close()
    return

while True:
    match menu():
        case 1:
            view_task()
        case 2:
            add_task()
        case 3:
            edit_task()
        case 4:
            Search_task()
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
        

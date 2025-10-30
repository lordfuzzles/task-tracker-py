import json,os,shutil

task_list = "./tasks.json"
menu = True

def main():
    try:
        with open(task_list, 'r') as file:
            pass
    except FileNotFoundError:
        os.system('echo "tasks": [] > ./tasks.json') 
    
    os.system("clear")

    test = input("What would you like to do?\n1. Print Tasks List\n2. Add Task\n3. Edit Task\n4. Exit\n")
    match test:
        case '1':
            print_list()
        case '2':
            add_task_menu()
        case '3':
            edit_task_menu()
        case '4':
            exit()
        case _:
            os.system("clear")
            print("Not a valid option")

def print_list():
    os.system("clear")
    print(f"""************************
*- Current Tasks List -*
************************""")
    with open(task_list) as read_file:
        read_data = json.load(read_file)
    
    for item in read_data['tasks']:
        print(f"{item['id']}. {item['name']} - Status: {item['status']} - Due: {item['dueDate']}")
    
    print(" ")
    input("Press any key to return to the menu...")

def add_task_menu():
    os.system("clear")
    task_name = input("What is the name of the task?\n")
    task_status = input("Have you started this task already?\n")
    task_due_date = ""

    match task_status[:1].lower():
        case "n":
            task_status = "Not started"
            task_due_date = input("When do you need to have this task done?\n")
        case "y":
            if input("Have you already completed this task?\n")[:1].lower() == "n":
                task_status = "In Progress"
                task_due_date = input("When do you need to have this task done?\n")
            elif input("Have you already completed this task?\n")[:1].lower() == "y": 
                task_status = "Completed"
            else:
                print("Something is wrong with you.")
        case _:
            print("That is not an option. Correct yourself.")

    
    print(f"{task_name} added. Current status: {task_status}. Due: {task_due_date}.")

    new_task = {
        "name": task_name,
        "status": task_status,
        "dueDate":task_due_date
    }

    add_task(new_task, task_list)


def edit_task_menu():
    os.system("clear")


def add_task(task_to_add, list):
    try:
        with open(list, mode='r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    
    task_to_add = {"id": len(tasks['tasks']) + 1} | task_to_add

    tasks['tasks'].append(task_to_add)

    with open(list, mode='w') as file:
        json.dump(tasks, file, indent=2)

    print(f"Task {task_to_add['name']} added to tasks list.")
    print(" ")
    input("Press any key to return to the menu...")

while menu == True:
    main()  
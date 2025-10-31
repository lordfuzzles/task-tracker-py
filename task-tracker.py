import json,os,shutil

list_file = "./tasks.json"

def main():
    while True:
        try:
            with open(list_file, 'r') as file:
                pass
        except FileNotFoundError:
            os.system('echo "tasks": [] > ./tasks.json') 
        
        os.system("clear")

        test = input("What would you like to do?\n1. Print Tasks List\n2. Add Task\n3. Edit Task\n4. Remove Task\n5. Exit\n\n> ")
        match test:
            case '1':
                print_list()
                return_main()
            case '2':
                add_task_menu()
            case '3':
                edit_task_menu()
            case '4':
                remove_task()
            case '5':
                exit()
            case _:
                os.system("clear")
                print("Not a valid option")

def return_main():
    print(" ")
    input("Press any key to return to the menu...")
    

def print_list():
    os.system("clear")
    print(f"""************************
*- Current Tasks List -*
************************""")
    task_list = open_task_list(list_file)
    
    for item in task_list['tasks']:
        print(f"{item['id']}. {item['name']} - Status: {item['status']} - Due: {item['dueDate']}")
    
    

def add_task_menu():
    os.system("clear")
    task_name = input("What is the name of the task?\n\n> ")
    task_status = input("Have you started this task already?\n\n> ")
    task_due_date = ""

    match task_status[:1].lower():
        case "n":
            task_status = "Not started"
            task_due_date = input("When do you need to have this task done?\n\n> ")
        case "y":
            if input("Have you already completed this task?\n\n> ")[:1].lower() == "n":
                task_status = "In Progress"
                task_due_date = input("When do you need to have this task done?\n")
            elif input("Have you already completed this task?\n\n> ")[:1].lower() == "y": 
                task_status = "Completed"
            else:
                print("Something is wrong with you.")
                return_main()
        case _:
            print("That is not an option. Correct yourself.")
            return_main()

    
    print(f"{task_name} added. Current status: {task_status}. Due: {task_due_date}.")

    new_task = {
        "name": task_name,
        "status": task_status,
        "dueDate":task_due_date
    }

    add_task(new_task, list_file)

    return_main()

def add_task(task_to_add, list):
    task_list = open_task_list(list_file)
    task_to_add = {"id": len(task_list['tasks']) + 1} | task_to_add
    task_list['tasks'].append(task_to_add)

    with open(list, mode='w') as write_file:
        json.dump(task_list, write_file, indent=2)

    print(f"Task {task_to_add['name']} added to tasks list.")

def edit_task_menu():
    task_list = open_task_list(list_file)

    os.system("clear")
    print_list()
    print(" ")
    task_select = int(input("Which task would you like to edit?\n\n> ")) - 1 
    task_to_edit = task_list["tasks"][task_select]

    return_main()


def remove_task():
    task_list = open_task_list(list_file)

    os.system("clear")
    print_list()
    print(" ")
    task_to_remove = int(input("Type the number of the task you would like to remove:\n\n> ")) - 1 
    removed_task = task_list["tasks"][task_to_remove]["name"]
    del task_list["tasks"][task_to_remove]

    confirm = input(f"Are you sure you want to remove {removed_task}? (y/n)\n\n> ")

    if confirm[0].lower() == "y":
        with open(list, mode='w') as write_file:
            json.dump(task_list, write_file, indent=2)
        print(f"Task {removed_task} removed from tasks list.")
    elif confirm[0].lower() == "n":
        print("Removal process aborted.")
    else:
        print("Input out of acceptable range.")
   
    return_main()

def open_task_list(list):
    with open(list, mode='r') as file:
        list_data = json.load(file)
    
    return list_data

main()  
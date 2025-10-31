import json

list_file = "./tasks.json"

new_entry = {
    "name": "Test",
    "status": "Not Started",
    "dueDate": "11/30/2025"
}

def open_task_list(list):
    with open(list, mode='r') as read_file:
        list_data = json.load(read_file)
    
    return list_data

task_list = open_task_list(list_file)

test_task_number = "2"

test_task = task_list["tasks"][int(test_task_number) - 1]

print(test_task["name"])

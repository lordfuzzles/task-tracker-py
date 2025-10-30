task_list = {
  "tasks": [
    {
      "id": 1,
      "name": "Build Lab",
      "status": "Not Started",
      "dueDate": "11/15/2025"
    },
    {
      "id": 2,
      "name": "Image Computer",
      "status": "Not Started",
      "dueDate": "11/20/2025"
    }
  ]
}

new_entry = {
    "name": "Test",
    "status": "Not Started",
    "dueDate": "11/30/2025"
}

print(len(task_list["tasks"]))

new_entry = {"id": len(task_list["tasks"]) + 1} | new_entry

print(new_entry)
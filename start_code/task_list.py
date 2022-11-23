tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# question 1

uncompleted_tasks = []
for task in tasks:
    if task["completed"] == False:
        uncompleted_tasks.append(task["description"])
print(uncompleted_tasks)

# question 2

completed_tasks = []
for task in tasks:
    if task["completed"] == True:
        completed_tasks.append(task["description"])
print(completed_tasks)

# question 3

descriptions_of_task = []
for task in tasks:
    descriptions_of_task.append(task["description"])
print(descriptions_of_task)

# question 4

def time_taken(time):
   for task in tasks:
       if time >= task["time_taken"]:
        print(task)

time_taken(20)

# question 5

def print_task_given_description(description):
    for task in tasks:
        if description == task["description"]:
           print(task)
print_task_given_description("Feed cat")

# question 6

# def descritption__update_to_complete(description):
#     for task in tasks:
    

# question 7
new_task = {"description": "Go Gym", "completed": False, "time_taken": 80 }
dict_copy = new_task.copy()
tasks.append(dict_copy)
print(tasks)


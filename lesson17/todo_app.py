from typing import List, Dict

tasks: List[Dict[str, str]] = []

def add_tasks(**task):
    if task in tasks:
        print(f'You did this task: {task} already, add task to the lists!')
        return
    else:
        tasks.append(task)
        print(f'You added task: {task["name"]} with definition: {task["definition"]} and priority: {task["priority"]} to the list.')
        print(tasks)


add_tasks(name="learn python", definition="OOP", priority="important")
add_tasks(name = "learn python", definition="inheritance", priority="important")

print(tasks)
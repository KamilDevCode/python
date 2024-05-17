tasks = []


def add_tasks(new_task=str, definition=str, priority=str):
    if not new_task.strip():
        print('You did not add task to the lists !')
        return
    else:
        tasks.append({"name": new_task, "definition": definition, "priority": priority})
        print(f'You added task: {new_task} with definition: {definition} and priority: {priority} to the list.')
        print(tasks)


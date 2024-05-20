#!/usr/bin/python3

"""Gathers data from an api"""

if __name__ == '__main__':
    import requests
    import sys

    employee_id = sys.argv[1]

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_id)
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    completed_task_count = 0
    total_tasks = 0
    task_names = []
    name = user.get('name')

    # extract information for the user with a matching employee id
    for todo in todos:
        if not todo.get('userId') == int(employee_id):
            continue
        total_tasks += 1
        if todo.get('completed'):
            completed_task_count += 1
        task_names.append(todo.get('title'))

    print('Employee {} is done with tasks({}/{}):'.format(
        name, completed_task_count, total_tasks))

    for task_name in task_names:
        print('\t {}'.format(task_name))

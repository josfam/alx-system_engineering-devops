#!/usr/bin/python3

"""Gathers data from an api"""

if __name__ == '__main__':
    import json
    import requests
    import sys

    employee_id = sys.argv[1]

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_id)
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    username = user.get('username')
    task_names = {employee_id: []}

    # extract task info for the user with a matching employee id
    for todo in todos:
        if not todo.get('userId') == int(employee_id):
            continue
        task_info = {
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': username
        }
        task_names.get(employee_id).append(task_info)

    output_file = f'{employee_id}.json'

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(task_names, f)

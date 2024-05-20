#!/usr/bin/python3

"""Gathers data from an api"""

if __name__ == '__main__':
    import json
    import requests
    import sys

    users_url = 'https://jsonplaceholder.typicode.com/users/'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    employee_data = {}

    # pluck all user ids and related usernames
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        starter_dict = {user_id: [{'username': username}]}
        employee_data.update(starter_dict)

    # pluck necessary task data
    for todo in todos:
        user_id = todo.get('userId')
        title = todo.get('title')
        completed = todo.get('completed')
        todo_info = {'task': title, 'completed': completed}
        username = employee_data.get(user_id)[0].get('username')

        if len(employee_data.get(user_id)[0]) == 1:
            employee_data.get(user_id)[0].update(todo_info)
        else:
            todo_info.update({'username': username})
            employee_data.get(user_id).append(todo_info)

    output_file = f'todo_all_employees.json'

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(employee_data, f)

#!/usr/bin/python3

"""Gathers data from an api"""

if __name__ == '__main__':
    import csv
    import requests
    import sys

    employee_id = sys.argv[1]

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_id)
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    name = user.get('name')
    all_tasks = []

    # extract information for the user with a matching employee id
    for todo in todos:
        if not todo.get('userId') == int(employee_id):
            continue

        task_summary = {
            "USER_ID": employee_id,
            "USERNAME": name,
            "TASK_COMPLETED_STATUS": todo.get('completed'),
            "TASK_TITLE": todo.get('title')
            }
        all_tasks.append(task_summary)


# construct, and write to the csv file, while quoting all strings
output_file = '{}.csv'.format(employee_id)

with open(output_file, 'w', encoding='utf-8') as f:
    field_names = [
        'USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    writer = csv.DictWriter(f, fieldnames=field_names, dialect='unix')
    for task in all_tasks:
        writer.writerow(task)

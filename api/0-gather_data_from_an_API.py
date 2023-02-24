#!/usr/bin/python3
""" Python Script that uses REST
 API to return information about his/her TODO list progress"""

import requests
import sys


def main():
    user_id = int(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'

    response = requests.get(todo_url)
    total_tasks = 0
    completed_tasks = []

    for task in response.json():
        if task['userId'] == user_id:
            total_tasks += 1
            if task['completed']:
                completed_tasks.append(task['title'])

    user_name = requests.get(user_url).json()['name']
    summary = f"Employee {user_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):"
    print(summary)

    for task in completed_tasks:
        print(f"\t{task}")


if __name__ == '__main__':
    main()

#!/usr/bin/python3
""" Python Script that uses REST
 API to return information about his/her TODO list progress"""

import requests
import sys

# Retrieve user ID from the command line arguments


def main():
    user_id = int(sys.argv[1])
# Defines the URLs for the API endpoints
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)


# Retrieve the list of tasks from the API
response = requests.get(todo_url)
# Initialize variables for tracking completed tasks and total tasks
total_tasks = 0
completed_tasks = []

for task in reponse.json():
    if task['userId'] == user_id:
        total_tasks += 1
        if task['completed']:
            completed_tasks.append(task['title'])

summary = f"Employee {user_name} is done with tasks({len(completed_tasks)} /
                                                    {total_tasks}): "
print(summary)

for task in completed_tasks:
    print(f"\t {task}")

if __name__ == '__main__':
    main()

#!/usr/bin/python3
"""A script that returns information about a given employee TODO list progress"""

import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    EMPLOYEE_NAME = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            TOTAL_NUMBER_OF_TASKS += 1
            if task.get('completed'):
                NUMBER_OF_DONE_TASKS += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    print('\n'.join(["\t " + task.get('TASK_TITLE') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('NUMBER_OF_DONE_TASKS')]))

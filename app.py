#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from classes.project import *
from utils import common

USER_CHOICE = """
Enter: 
- 'a' to add a new project
- 'c' to print the current project
- 'l' to list all projects
- 'd' to delete a project
- 'q' to quit
"""


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            print("Add a new Project")
            prompt_add_project()
        elif user_input == 'c':
            print("Print the Current Project")
        elif user_input == 'l':
            print("List all the projects")
        elif user_input == 'd':
            print("Delete a Project")
        else:
            print(f"Unknown command. Please try again.")
        user_input = input(USER_CHOICE)


# TODO: Create regex to validate the input fields
def prompt_add_project():
    name = input('Enter the project name must be different from ' ': ')
    while len(name) == 0:
        name = input('Enter the project name must be different from ' ': ')
    description = input('Enter the project description must be different from ' ': ')
    while len(description) == 0:
        description = input('Enter the project description must be different from ' ': ')
    token = input('Enter the Auth Token must be different from ' ': ')
    while len(token) == 0:
        token = input('Enter the Auth Token must be different from ' ': ')
    headers = common.prepare_headers(token)
    payload = common.prepare_project(name, description)

    project = Project(name, description, headers, payload)
    status = project.create()
    try:
        print(f"Project Name: {name} ")
        status = 'Created' if status['status'] == 'succeeded' else 'Not Created'
        print(f"Project status: {status} ")
    except Exception as err:
        print(f"Some error occurred: {err}")


if __name__ == "__main__":
    menu()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from classes.project import *
from utils import common
import re

USER_CHOICE = """
Enter: 
- 'a' to add a new project
- 'f' to find a project
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
        elif user_input == 'f':
            get_project()
        elif user_input == 'c':
            print("Print the Current Project")
        elif user_input == 'l':
            print("List all the projects")
            list_projects()
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


def list_projects():
    print("Listing the projects")
    token = input('Enter the Auth Token must be different from ' ': ')
    while len(token) == 0:
        token = input('Enter the Auth Token must be different from ' ': ')
    headers = common.prepare_headers(token)
    projects = Project.get_all(headers, payload={})
    print(f"There are {projects['count']} project(s) created!")
    for project in projects['value']:
        print(f"PROJECT: {project['name']} | VISIBILITY: {project['visibility']} | URL: {project['url']}\n")
        # print(f"Project id: {project['id']}")
        # print(f"Project Name: {project['name']}")
        # print(f"Project Description: {project['description']}")
        # print(f"Project State: {project['state']}")
        # print(f"Project Visibility: {project['visibility']}")
        # print(f"Project Revision: {project['revision']}")
        # print(f"Project Last Update Time: {project['lastUpdateTime']}")
        # print(f"Project Url: {project['url']}")


# TODO: Need to filter with another attribute and get the correct project url
# ex: https://dev.azure.com/douglasqsantos/_apis/projects/2815357b-c36f-47d6-b87b-c86dabd0e8c2
"""
{
  "id": "2815357b-c36f-47d6-b87b-c86dabd0e8c2",
  "name": "Fel",
  "description": "Fel",
  "url": "https://dev.azure.com/douglasqsantos/_apis/projects/2815357b-c36f-47d6-b87b-c86dabd0e8c2",
  "state": "wellFormed",
  "revision": 221,
  "_links": {
    "self": {
      "href": "https://dev.azure.com/douglasqsantos/_apis/projects/2815357b-c36f-47d6-b87b-c86dabd0e8c2"
    },
    "collection": {
      "href": "https://dev.azure.com/douglasqsantos/_apis/projectCollections/8c0284a5-92e5-4c56-b7a5-e5d6debd055e"
    },
    "web": {
      "href": "https://dev.azure.com/douglasqsantos/Fel"
    }
  },
  "visibility": "private",
  "defaultTeam": {
    "id": "6a533b03-d4bf-4632-9198-ddbf646b1c9b",
    "name": "Fel Team",
    "url": "https://dev.azure.com/douglasqsantos/_apis/projects/2815357b-c36f-47d6-b87b-c86dabd0e8c2/teams/6a533b03-d4bf-4632-9198-ddbf646b1c9b"
  },
  "lastUpdateTime": "2021-01-07T01:52:56.107Z"
}
"""


def get_project():
    token = input('Enter the Auth Token must be different from ' ': ')
    while len(token) == 0:
        token = input('Enter the Auth Token must be different from ' ': ')
    looking_for = input('Enter the Project Name you are looking for: ')
    headers = common.prepare_headers(token)
    projects = Project.get_all(headers, payload={})
    pattern = f'^.*{looking_for}.*$'
    found = []
    for project in projects['value']:
        match = re.search(pattern, project['name'], re.IGNORECASE)
        if match:
            found.append(project)

    if found:
        for project in found:
            print(f"PROJECT: {project['name']} | VISIBILITY: {project['visibility']} | URL: {project['url']}\n")
    else:
        print(f"No Project Found")


if __name__ == "__main__":
    menu()
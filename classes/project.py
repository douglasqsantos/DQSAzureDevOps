#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .azuredevops import *


class Project:
    def __init__(self, name, description, headers, payload):
        self.name = name
        self.description = description
        self.headers = headers
        self.payload = payload

    def __repr__(self):
        return f"<Project {self.name} - {self.description}"

    def __str__(self):
        return f"<Project {self.name} - {self.description}"

    def create(self):
        project = AzureDevOps(self.headers, self.payload)
        return project.post_request()

    def get_current(self):
        return self.payload

    def delete(self):
        pass

    def get_all(self):
        pass

    def get_by_id(self):
        pass

    def get_by_name(self):
        pass

    def get_by_description(self):
        pass

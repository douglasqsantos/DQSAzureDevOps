#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from requests.exceptions import HTTPError
import json
import time


class AzureDevOps:
    def __init__(self, headers, payload):
        self.url = "https://dev.azure.com/douglasqsantos/_apis/projects?api-version=5.0"
        self.headers = headers
        self.payload = payload

    def __repr__(self):
        return f"<AzureDevOps Handler Class>"

    def __str__(self):
        return f"<AzureDevOps Handler Class>"

    @staticmethod
    def _handle_request(method, url, headers, payload):
        try:
            if method == "POST":
                response = requests.request(method, url, headers=headers, data=json.dumps(payload))
            elif method == "GET":
                payload = {}
                response = requests.request(method, url, headers=headers, data=payload)
            else:
                raise NotImplementedError
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except NotImplementedError as err:
            print(f"Method Not implemented yet: {err}")
        except HTTPError as http_err:
            return f'HTTP error Occurred: {http_err}'
        except Exception as err:
            return f'Other error occurred: {err}'
        else:
            return response.json()

    def post_request(self):
        try:
            create_project = self._handle_request("POST", self.url, self.headers, self.payload)
            try:
                # noinspection PyTypeChecker
                if create_project['url']:
                    # noinspection PyTypeChecker
                    status = self._handle_request("GET", create_project['url'], self.headers, self.payload)
                    # noinspection PyTypeChecker
                    while status['status'] != 'succeeded':
                        time.sleep(1)
                        # noinspection PyTypeChecker
                        status = self._handle_request("GET", create_project['url'], self.headers, self.payload)
                    return status
            except Exception as err:
                return f'Other error occurred: {err}'
        except Exception as err:
            return f'Other error occurred: {err}'

    def get_request(self):
        try:
            projects = self._handle_request("GET", self.url, self.headers, self.payload)
            return projects
        except Exception as err:
            return f'Other error occurred: {err}'

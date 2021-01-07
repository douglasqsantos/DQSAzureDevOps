#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64


def _prepare_token(token):
    base_token = 'Basic:' + token
    token = base64.b64encode(base_token.encode()).decode()
    return 'Basic ' + token


def prepare_headers(token):
    return {
        'Content-Type': 'application/json',
        'Authorization': _prepare_token(token)
      }


def prepare_project(name, description):
    """
    :param name: Project Name
    :param description: Project Description
    :return: Project Template
    """
    return {
        'name': name,
        'description': description,
        'capabilities': {
            'versioncontrol': {
                'sourceControlType': 'Git'
            },
            'processTemplate': {
                'templateTypeId': '6b724908-ef14-45cf-84f8-768b5384da45'
            }
        }
    }

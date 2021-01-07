#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def project_template(name, description):
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

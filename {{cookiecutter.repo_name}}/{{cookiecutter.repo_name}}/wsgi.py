#!/usr/bin/env python2
# coding=utf-8

"""
wsgi app from paste deploy
"""

from paste.deploy import loadapp

import {{ cookiecutter.repo_name }}.config_logger

application = wsgi_app = loadapp('config:/opt/{{ cookiecutter.repo_name }}/conf/paste.ini')

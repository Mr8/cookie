#!/usr/bin/env python
# encoding: utf-8


from pkg_resources import resource_filename
from logging.config import fileConfig


fileConfig(resource_filename("{{ cookiecutter.repo_name }}", "logger.conf"))

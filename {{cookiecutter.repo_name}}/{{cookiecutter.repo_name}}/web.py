#!/usr/bin/env python
# encoding: utf-8

"""Web API of {{ cookiecutter.repo_name }} """

import logging
from bottle import default_app, route, run

logger = logging.getLogger(__name__)

app = default_app()
application = app

def app_factory(global_config, **local_conf):
    return app


@route('/')
def index():
    '''Home'''
    return "{{ cookiecutter.repo_name }} web interfaces"


def main(host='localhost', port=8080):
    run(app=application, host=host,
        port=port, reloader=False, quite=True)


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 2:
        main(host=sys.argv[1])
    elif len(sys.argv) == 3:
        main(host=sys.argv[1], port=int(sys.argv[2]))
    else:
        main()

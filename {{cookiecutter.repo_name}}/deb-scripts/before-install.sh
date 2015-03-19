#!/bin/sh
set -e

stop_upstart_service_maybe() {
	service="$1"
	if [ -e /etc/init/${service}.conf ]; then
		if status "$service" |grep 'start/running'; then
			stop "$service" || true
		fi
	fi
}

cd /
stop_upstart_service_maybe {{ cookiecutter.repo_name }}

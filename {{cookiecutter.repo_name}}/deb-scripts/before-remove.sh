#!/bin/sh
set -e

PREFIX=${PREFIX:-/opt/{{ cookiecutter.repo_name }}}

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

# delete installed cron jobs, upstart config files, and binaries.
rm -f /etc/logrotate.d/{{ cookiecutter.repo_name }}
rm -f /etc/init/{{ cookiecutter.repo_name }}.conf
rm -f /etc/sudoers.d/{{ cookiecutter.repo_name }}

if [ -d "$PREFIX" ]; then
	make -C "$PREFIX" full-clean
fi

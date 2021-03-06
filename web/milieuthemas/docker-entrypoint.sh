#!/usr/bin/env bash

set -u
set -e

METADATA_HOST=169.254.169.254
METADATA_PORT=80
METADATA_URL=http://${METADATA_HOST}:${METADATA_PORT}/latest/meta-data/local-ipv4

export DOCKER_IP=$(hostname --ip-address)

#Check connectivity
curl -s -m1 ${METADATA_URL} || exitcode=$?
if [ -n "${exitcode+set}" ]; then
  export DOCKER_EXTERNAL_IP=${DOCKER_IP}
else
  export DOCKER_EXTERNAL_IP=$(curl ${METADATA_URL})
fi

cd /app

# collect static files
python manage.py collectstatic --noinput

# run uwsgi
exec uwsgi

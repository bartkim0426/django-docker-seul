#! /bin/bash
sleep 8; echo "*** Waiting for webapp container ..."

envsubst < nginx-dev.tmpl > /etc/nginx/nginx.conf

nginx -g "daemon off;"

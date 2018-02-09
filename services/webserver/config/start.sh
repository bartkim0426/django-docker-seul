#! /bin/bash
sleep 25; echo "*** Waiting for webapp container ..."
envsubst < nginx.tmpl > /etc/nginx/nginx.conf

nginx -g "daemon off;"

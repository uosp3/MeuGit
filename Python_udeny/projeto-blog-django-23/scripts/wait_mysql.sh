#!/bin/sh

while ! nc -z $MYSQL_HOST $MYSQL_PORT; do
  echo " Waiting for MYSQL Database Startup ($MYSQL_HOST $MYSQL_PORT) ..."
  sleep 1
done

echo " MYSQL Database Started Successfully ($MYSQL_HOST:$MYSQL_PORT)"

#!/bin/sh

# o shell ira encerrar a execução do script quando um comando falhar
set -e

wait_mysql.sh
collectstatic.sh 
migrate.sh
runserver.sh
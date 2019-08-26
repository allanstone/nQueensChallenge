#!/bin/bash

# Script to commit after running tests for the project
# set virtualenv
venv=venv/bin/activate
if [ -f "$venv" ]
then
    echo the file exists
    source $venv
else
    echo the file does not exist
    virtualenv venv -p `which python3`
fi
# run all unitest 
py.test  nQueensChallenge/tests/ \
  --sqlalchemy-connect-url="postgres+psycopg2://postgres:post123@localhost:5432/testdb" \
  -p no:warnings -v || { echo 'pytest run fail' ; exit 1; }
# Updating files in local Repo
git status
# unset this to pass the ssh auth
unset SSH_ASKPASS
read -p "Commit description: " desc
# if empty desc will be 'Backup dd/mm/yy' 
desc=${desc:-Save}
desc+=$(date +" %d/%m/%y")
git add -A && \
git commit -m "$desc" && \
read -p "Push to master? (y/n)" answ
echo    # (optional) move to a new line
if [[ $answ =~ ^[Yy]$ ]]
then
    git push -u origin master
fi

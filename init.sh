#!/bin/bawsh
L='X'
PN='proyecto'
APP='aplicacion'
BD='examen'
#git archive --format zip --output ../examen$L.zip master

django-admin.py startproject $PN
cd $PN
python manage.py startapp $APP
echo 'FILE: '$PN'/settings.py: añadir' $APP 'al final de la lista INSTALLED_APPS'

export DATABASE_URL='postgres://alumnodb:alumnodb@localhost:5432/'$BD''
createdb -U alumnodb -h localhost $BD
#dropdb -U alumnodb examen
echo falta python database_cleaner.py
export SQLITE=1

echo web: gunicorn $PN.wsgi --log-file - >> Procfile
echo python-2.7.14 >> runtime.txt

pip freeze > requirements.txt
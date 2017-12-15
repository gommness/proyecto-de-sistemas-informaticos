#!/bin/bawsh
L='X'
PN='proyecto'
APP='aplicacion'
BD='examen'
#git archive --format zip --output ../examen$L.zip master

django-admin.py startproject $PN
cd $PN
python manage.py startapp $APP
echo "database password for drop:"
dropdb -U alumnodb examen
echo "database password for create:"
createdb -U alumnodb -h localhost $BD

echo -e "TODO:\n"
echo "export SQLITE=1"
echo "export DATABASE_URL='postgres://alumnodb:alumnodb@localhost:5432/$BD'"
echo 'FILE: '$PN'/settings.py: añadir' $APP 'al final de la lista INSTALLED_APPS'
echo 'FILE: $PN/settings.py: añadir DATABASES'

echo web: gunicorn $PN.wsgi --log-file - >> Procfile
echo python-2.7.14 >> runtime.txt

#pip freeze > requirements.txt

echo "loremipsum==1.0.5
selenium==3.7.0
dj-database-url==0.4.2
dj-static==0.0.6
Django==1.11.5
Pillow==2.3.0
psycopg2==2.7.3.1
static3==0.7.0
gunicorn==19.6.0" > requirements.txt
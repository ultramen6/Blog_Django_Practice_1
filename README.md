# Blog_Django_Practice_1
first_django_project


Для начала, создание репозитория на гит хабе:

[GitHub](https://github.com/ultramen6/Blog_Django_Practice_1)

Стандартные манипуляции в bash:

```console
/mnt/c/Dev$
git init git@github.com:ultramen6/Blog_Django_Practice_1.git
cd Blog_Django_Practice_1/
```
виртуальная среда:
```console
python3 -m venv venv
source venv/bin/activate
```
Установка django
```console
pip install django
touch requirements.txt
pip freeze
```
добавление пакетов в requriments.txt
```console
nano requirements.txt
asgiref==3.5.2
Django==4.0.5
sqlparse==0.4.2
```
стартуем проект Blog
```console
django-admin startproject Blog
```
далее, открываю VSC через code . 

*Первичная настройка завершена*
сохраню redmi и сделаю первый коммит 

```console
git add .
git commit -m 'text'
git push
```


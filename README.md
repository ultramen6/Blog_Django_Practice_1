# Blog_Django_Practice_1
first_django_project

Этот проект воссоздан с ютуб канала:   
[Youtube](https://www.youtube.com/watch?v=T0Xi8gWDrQ0&list=PLlWXhlUMyooaDkd39pknA1-Olj54HtpjX&index=1)    
Первой целью - является полный разбор ( свои авторские умозаключения , выводы и вся   остольная 'вода' вроде этой) и наидетальнейший конспект почти каждого момента,   воспроизведенным автором видео, коненчо же в моей редакции, как ученика, находящегося   на лекции. Если хватит сил и терпения расписывать все 14 уроков на столько подробно, как   первый, не исключаю дополнительные отдельные погружения в документацию или другие   ссылки на других авторов по разъяснению конкретных моментов. Так же планировал   проанализировать код самой библиотеки, если получится, хотя бы на те классы и функции,   которые используются в проекте как минимум.  
Второй - обучение и дисциплина записи проектов в MD файл, создание супер кратких тезисов   для карточек Anki.   
[AnkiWeb](https://ankiweb.net)  

Критика, вопросы, пожелания - https://t.me/Ultramen6  



Для начала, создание репозитория на гит хабе:

[GitHub](https://github.com/ultramen6/Blog_Django_Practice_1)

Стандартные манипуляции в bash:

```console
/mnt/c/Dev$
git init git@github.com:ultramen6/Blog_Django_Practice_1.git
cd Blog_Django_Practice_1/
```
Виртуальная среда:
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
Добавление пакетов в requriments.txt
```console
nano requirements.txt
asgiref==3.5.2
Django==4.0.5
sqlparse==0.4.2
```
Стартуем проект BlogEngine
```console
django-admin startproject BlogEngine
```
Далее, открываю VSC через code .   

*Первичная настройка завершена*  
Сохраню redme и сделаю первый коммит 

```console
git add .
git commit -m 'text'
git push
```

Внутри папки BlogEngine:
```console
./python manage.py startapp Blog
```

### Роутинг запросов - 1 часть

Джанго работает по модели - MVC  
Model  
View  
Controller  

Суть заключается в том, что код раздельный для DB , для ответа пользователям (View), и отдельная обработка перед отправкой к пользователю (controller)  

**urls.py** - отвечает за маршрутизацию пользователей  
**views.py** - отвечает за обработку запроса от пользователя  
**models.py** - отвечает за хранине данных в DB  

В этом проекте будет по умолчанию использоваться SQLite3 DB.  
Сразу применяем новые миграции для БД (далее будут разъяснения)  

```console
./manage.py migrate
``` 
запуск тестового сервера
```console
./manage.py runserver 8000
```

Что сделал джанго когда мы перешли по локальной ссылке в браузер с запущенным сервером ?     
Наш браузер сгенерировал запрос в объект request, который попал к нам в приложение.    
Задача - принять запрос и отправить его в обработчик.  

Переходим в **urls.py** , видим *urlpatterns* переменную, являющююся списком результата работы функции Path. Добавляем новый элемент для наглядности:  

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', hello)
]
```
На данный момент функции hello пока что нет, добавим ее из !будущего файла .views:
```python
from .views import hello
```
Создаем views.py в папке с корневым проектом BlogEngine.  
Внутри создаем запрашиваемую функцию hello:  
```python
def hello(request):
    pass
```
*Надо иметь ввиду*, что все функции обработчики, принимают обязательный аргумент request,   который генерит нам браузер.  
Перезапускаем сервер, и видим, что все пока что работает без исключений, но до момента,   пока мы не переходим в браузере по адресу /localhost/8000/blog/.  
Конечно же, ловим исключение, потому, что у нас еще пустая функция hello.  
*Надо иметь ввиду*, что в браузере мы переходим по имени blog/, это имя и есть в ранее   указанной переменной urlpatterns:  
```python 
path('blog/', hello)
```
Чего мы добились на данном этапе? - мы поняли, что запрос пользователя, объект request   прошел через файл **urls.py**, через переменную urlpatterns, был определен маршрут /blog,   и этот объект был отправлен в функцию hello на обработку, куда он попал, и джанго   сгенерировал исключение.  

Временно наполнил функцию hello для анализа в консоли, после запуска исключения:  
```python
def hello(request):   
    print()
    print(request)
    print()
    print(dir(request))
    print()
    pass
```
Получаем в консоли ответ:
```console
<WSGIRequest: GET '/blog/'>

['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_current_scheme_host', '_encoding', '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_read_started', '_set_content_type_params', '_set_post', '_stream', '_upload_handlers', 'accepted_types', 'accepts', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_signed_cookie', 'headers', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user']
```

Из первой строчки видно, что объект request содержит в себе Http запрос GET, и по какому   адресу произошел этот запрос /blog/. Это показывает наглядно, что этот запрос пришел во   **views.py** потому, что внутри этого файла наша функция hello вывела эти запросы с   dir().
Таже функция dir() вывела все методы списком, некоторые методы мы будем использовать -   к примеру GET, словарь POST. Мораль такова, что можно посмотреть всегда все обьекты request   и нетолько с помощью dir().  

Настало время вернуть джанго нормальный ответ пользователю, для этого импортируем в   views.py модуль HttpResponse.   
Возвращаем ответ в виде заголовка первого уровня.  

```python
from django.http import HttpResponse


def hello(request):
    return HttpResponse('<h1>Hello World</h1>')
```

Стоит начать делать как нужно, по этому, *инициализируем новое приложение* (ранее мы   создали его, оно называется Blog) в settings.py, в папке BlogEngine.  
```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'Blog'
]
```
Добавляем название приложения Blog и все...  

Далее редактируем корневой файл **urls.py**   
Немного подробней про функцию Path:  
```python 
path('blog/', hello)
```
Она может принимать 4 аргумента:   
1- шаблон урла.  
2- функция - обязательный аргумент. Она будет обрабатывать запрос по адресу в первом   аргументе ( к примеру /blog/).  
3- имя.  
4- доп параметры, которые дальше передадутся в функцию в виде словаря.  

Пока остановимся на этих двух.  
На самом деле 2-ой аргумент может быть и не явным и не функцией, а к примеру более точный   файл urls path, в котором более детальная маршрутизация. Потому, что у приложения   (в частности блога) может быть много страниц. Посты, комменты, тэги итд. Все   это будет относиться к одному приложению /blog/, но иметь другую детализацию по доп. адресу.  
Что бы не нагромождать кучу юрл адресов, джанго может настраивать это более тонким образом.  
Для того, что бы джанго указать более детальную маршрутизацию запросов, необходимо   использовать функцию include.  
```python
from django.urls import include
```
Вместо функции hello, используем include, в качестве аргумента, в виде строки, мы используем   !будущий файл **urls.py** из приложения blog.  
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('Blog.urls'))
]
```
Старый импорт можно закоментировать и удалить.    
```python
#from .views import hello
```
Далее, создаем недостающий файл **urls.py** в приложении Blog.  
После дублируем код в новом файле урлов.   
```python
from django.urls import path

from .views import *


urlpatterns = [
	path('', posts_list)
]
```
Создали переменную urlpatterns. Внутри path создаем !будущую функцию posts_list (   произвольное название ), далее, в **views.py** импортируем HttpRespons, создаем функцию   posts_list, и по аналогии со старой функцией hello, передаем заголовок первого уровня:  
```html
'<h1>Hello World</h1>'
```
```python
from django.shortcuts import render
from django.http import HttpResponse


def posts_list(request):
    return HttpResponse('<h1>Hello World</h1>')
```
Далее, перезагружаем сервер и открываем http://127.0.0.1:8000/blog/  
Видим, что изменения никак не повлияли на приложение. Но теперь мы обращаемся с ответной   функцией из приложения Blog, а не из корневой папки.  
  
Посмотрим как джанго берет маршрутизацию на примере **urls.py** в корневой папке:  
Предположим, что из запроса по адресу http://127.0.0.1:8000/blog/something  
Джанго не трогает домен, получает такой кусок:  
/blog/something - этот кусочек обращается в **urls.py**, куда попадает в urlpatterns в   цикле, и проверяется соответствие полученного урла тому шаблону , который имеется в   списке    (**/blog/**something). Он находит этот шаблон, понимает что мы указали отдельную   функцию include, куда джанго отправляет остаток адреса **/something** в **  urls.py** приложения Blog.  
Конечно же **/something** после отправки в **urls.py**, снова попадает в urlpatterns.   Джагшл начинает опять сравнивать этот адрес с тем, что в списке urlpatterns. И НИЧЕГО не находит:  
```python
urlpatterns = [
	path('', posts_list)
]
```
Не находит потому, что у нас здесь ничего и нет, подходящее под **/something**.  
Мы же здесь определили пустую строку **path('',**.   
Вот как джанго на данном этапе маршрутизирует запросы.  

**END** 

Cохраню redme и сделаю коммит.   

```console
git add .
git commit -m 'text'
git push
```

### Шаблоны, наследование шаблонов - 2 часть.  

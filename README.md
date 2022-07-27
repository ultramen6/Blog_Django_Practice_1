# Blog_Django_Practice_1
first_django_project

Проконспектированы *2* из *13* частей.  
Примерное затраченное время на MD и самого кода: **6.5 часов**. ( 07-07-2021)  

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

Суть заключается в том, что код раздельный для DB (Model) , для ответа пользователям (View), и отдельная обработка перед отправкой к пользователю (controller)  

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
Конечно же **/something** после отправки в **urls.py**, снова попадает в urlpatterns.   Джанго начинает опять сравнивать этот адрес с тем, что в списке urlpatterns. И НИЧЕГО не находит:  
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

Начнем с **views.py** приложения Blog:  
Используя джанговый HttpRespone в виде фунуции, с заголовком, особо много не поиспользуешь. Для нормальной работы потребуется *html* странички, с которыми будет удобней работать, да и вообще, по-другому никак)  
Эти Html страницы наполняются данными ( верстка ) и отправляются пользователям.  
Создадим *html* шаблон(ы):  
В приложении Blog, создаем папку *tepmlates*, внутри нее папку *Blog*.   
Сделано это потому, что бы не было конфликтов шаблонов с одинаковыми названиями, эти шаблоны распределяются по папкам с названием привязанного шаблона приложения.  

Создаем **index.html** в teplates/Blog   
Находим на гитхабе стандартный текст:   [UPD: можно и на бутсрапе сразу]   

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="x-ru-compatible" content="ie=edge">
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>

    <link rel="stylesheet" href="https://fonts.googleapis.com/fonts">
    <link rel="stylesheet" href="css/style.css">
  </head>
  <body>
  </body>
</html>
```
Добавляем название вкладки и пару строк в тело, под h1 и h2 заголовками:  
```html
   <title>Index Page</title>

   <body>
        <h1>Hello world</h1>
        <h2>text</h2>
   </body>
```
Далее, проверим что получилось в браузере, но сначала в файле **Blog/views.py** убираем HttpResponse и используем функцию render, которая была создана автоматически при создании приложения.  
```python
from django.shortcuts import render


def posts_list(request):
    return render(request, 'blog/index.html')
```
Тестим на сервере. http://127.0.0.1:8000/blog/   

Далее, для того что бы отправить пользователю какие-то данные, мы можем передать к примеру, значения словаря:  
```python
def posts_list(request):
    n = 'asdklfasdkfljgh' # условный словарь
    return render(request, 'blog/index.html', context={'name': n}) 
    """ передаем в функцию render 3-ий аргумент context, 
    в котором к словарю назначаем ключ с названием 'name' для нашей переменной n.
```
**Важно**, ключ *name* - это та самая переменная, которая будет использоваться в шаблоне html.   
Добавляем в теги шаблона *html* нашу переменную:  
Конструкция {{ }} как раз для этого и существет:  
```html
 <body>
        <h1>Hello world</h1>
        <h2>text</h2>
        <p>
            {{ name }}
        </p>
```
Можно увидеть результат в браузере. В случае, если переменная в *html* шаблоне, и в коде функции не будет правильно называться, тогда не будет исключений джанго, он просто ничего не выведет.   
*Процесс наполнения шаблонов html данными называется rendering*  

Мы можем передать список функции render:  
```python
def posts_list(request):
    n = ['a','b','c','d'] 
    return render(request, 'blog/index.html', context={'name': n}) 
```
Он конечно же отобразится списком в *html*.  
Что бы сделать отображение вертикальным списком надо его обработать циклом.  
(я бы раньше подумал, что это внутри фунции render надо было бы делать xD)  
Но, нет, джанго умеет делать так: (P.S я на самом деле пока не знаю, но может и не только джангд так умеет)  
```html
<body>
        <h1>Hello world</h1>
        <h2>text</h2>
        
        {% for name in names %}  <!-- % - указание цикла -->
            <p>
                {{ name }}
            </p>
        {% endfor %}             <!-- % - указание завершения цикла -->
        
  </body>
```
Разжевываю что делает джанго. Он начинает цикл в указаном месте по стандартному питонячему циклу, элемент списка *name* внутри списка *names* итерируется. На каждой итерации он "оборачивается" заголовком <p></p>  
Можно посмотреть результат в браузере.   
**Обрати внимание**, что в функции render название ключа осталось name, в html название names.  
Пару слов об *html* страницах в приложении - если приложение не состоит из одной зарендеренной странички, и есть разная детализация внутри приложения, то использовать одну главную *html* страничку было бы не разумно, так как постоянно бы пришлось ее менять под разные задачи. Для этого в джанго есть **Шаблонизатор**, который позволяет наследоваться от *html* странички.  

Создадим *html* файл *base_blog.html* в templates/Blog/  
Из базового шаблона *index.html* переносим содержимое в *base_blog.html*, убираем все частности, оставить общие элементы.  ( как изначальный шаблон )  

Сразу добавим стили с bootstrap:  
[BootStrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/)    
Для начала надо поключить его добавив:  
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" 
     rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
  </head>
  <body>
  </body>
</html>
```
Затем, сразу возьмем навигационный бар:  
```html
<nav class="navbar navbar-expand-lg bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled">Disabled</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
```
Убираем выпадающий список в этом скопированном баре:    
```html
              <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Dropdown
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Something else here</a></li>
                </ul>
              </li>
```
Меняем цвет бара, берем на бутстрапе такой стиль:  
style="background-color: #e3f2fd  

Находим строчку в новом *html* шаблоне:  
```html
<nav class="navbar navbar-expand-lg bg-light">
```
Замена на:  
```html
<nav class="navbar navbar-expand-lg" style="background-color: #e3f2fd;">
```

Теперь надо разметить страничку для данных под частности:  
Расстановка для таких мест осуществляется с помощью блоков {% block title%} и конец блока {% endblock %}  
Применим сразу на примере:  
```html
<title>
    {% block title %}
        Blog Engine
    {% endblock %}
</title>
<!-- в конце массива -->
</nav>

        {% block content %}
            CONTENT
        {% endblock %}

  </body>
```
Можно было бы сравнить это все с анкетой, где есть заполненные места, и незаполненные.  
Далее, можно спокойно в *index.html* убрать все, кроме частностей:  
```html
<!-- добавляем вначале эту строчку, что бы все работало -->
{% extends 'Blog/base_blog.html' %}
<!-- расширение переадресуется в шаблон base_blog.html -->

{% block title%}
    Posts list
{% endblock %}


{% block content %}
    {% for name in names %}
        <p>
            {{ name }}
        </p>
    {% endfor %}
{% endblock %}
```
В итоге, сразу несколько действий должно быть осуществленно, добавить -  
{% extends 'Blog/base_blog.html' %}  
И после можно скопировать указаные ранее блоки с раширениями из *Blog/base_blog.html*  
Внутрь блока с пометкой content отправим ранний цикл со списком из старого *index.html*  

Немного меняем верстку:  **tip and trick**  

выделяем нижний кусок в *base_blog.html*  
{% block content %}  
    CONTENT  
{% endblock %}  
Не снимая это выделение производим такие действия -    
в VSC:     
Open command palette (usually Ctrl+Shift+P)    
Execute Emmet: Wrap with Abbreviation  

В открывшейся командной строке вводим:  
**.continer>.row>.col-6.offset-md-2**  
Таким образом, мы обернули наш блок дополнительной бутстраповской версткой. ( вообще топ фича )  
```html
<!-- получился такой код -->
<div class="continer">
    <div class="row">
        <div class="col-6 offset-md-2">
            {% block content %}
                CONTENT
            {% endblock %}
        </div>
    </div>
</div>
```
***Еще одно расширение:***  
Launch VS Code Quick Open (Ctrl+P)  
paste ext install htmltagwrap and enter  
select HTML  
press Alt + W (Option + W for Mac).  

Оно немного попроще, но тоже полезное.  
Еще добавим отступ:  
```html 
<div class="continer mt-5"> <!-- margin top 5 -->
```
Ну и добавим заголовок к нашему списку внутри *index.html*  
```html
{% block content %}
    <h1 class="mb-5">Posts:</h1>   <!-- вот он (mb-5 margin bottom) -->
    {% for name in names %}
        <p>
            {{ name }}
        </p>
    {% endfor %}
{% endblock %}
```
Все эти манипуляции с шаблоном нам дают некую свободу действий, что если нам надо что то поменять или добавить, мы будем создавать другие шаблоны, наследуясь от базовых и разом менять все что нужно и по нужным блокам, не переписывая тонны *html* страниц. Джанго хорош, в общем. ( а что будет потом с бд, вообще кайф )   

Еще осталось поправить структуру шаблонов, так как у нас нет сейчас общего шаблона на все приложения в одной стилистике, для этого:  
Создаем папку в корневой папке с названием templates ( прям в той, где находятся Blog, blog engine). Внутри этой папки создаем шаблон *base.html*   
Далее, из *base_blog.html* переносим весь код в новый файл. Это и будет базовым шаблоном для всех приложений.  
*base_blog.html* ( который пустой ) теперь по аналогии с *index.html* будет расширением для нашего основного шаблона:  
```html
{% extends 'base.html' %}
```
Если мы обновим страницу в браузере, тогда словим исключение о том, что джанго не видит этот шаблон; так как мы не добавили этот шаблон - добавляем:  
Переходим в основную папку *BlogEngine/settings.py* и внутри этого фала - находим переменную *TEMPLATES*  
В ключ 'DIRS' добавляем наш путь до шаблона:  
```Python
'DIRS': [
            Path.joinpath(BASE_DIR, 'templates')
        ]
'''BASE_DIR является глобальной переменной, которая находится выше. Эта переменная указывает путь до приложения.'''
```
Можно это проанализировать в консоли, для этого надо перейти в папку с этим файлом *settings.py*, а то абсолютный путь будет неверным:  
```console
/mnt/c/Dev/Blog_Django_Practice_1/BlogEngine$ cd BlogEngine/
/mnt/c/Dev/Blog_Django_Practice_1/BlogEngine/BlogEngine$ python

Python 3.9.2 (default, Feb 28 2021, 17:03:44)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.

from pathlib import Path
>>> base = Path('settings.py').resolve().parent.parent
>>> base
PosixPath('/mnt/c/Dev/Blog_Django_Practice_1/BlogEngine')
>>> Path.joinpath(base, 'templates')
PosixPath('/mnt/c/Dev/Blog_Django_Practice_1/BlogEngine/templates')
>>>
```
Вот так эта ссылка с абсолютным путем ведет джанго проект, затем функция Path.joinpath добаляет 'templates', и шаблон становится видимым.   
Проверяем в браузере.   

<END> 

СОЗДАТЬ КАРТОЧКИ АНКИ ПО 2 УРОКУ - *выполнено*

### Создание модели Post, шаблоны Index, Detail - 3 часть.  

Как выглядет БД на простом примере в excel:
```excel
Post - название таблички

поля:
Id , title, body, slug, tags
1
2
3
4
5
```
Что бы не писать специфический код , который работает в БД , в джанго есть   
ORM модели ( Object relation mappin)- Это наложение обьектов языка Python   
на реляционную модель БД.  
ORM - это некий абстрактный слой логики, который позволяет описывать данные,  
которые будут храниться в БД в виде классов языка (Python), такие классы  
называются - моделями. Верхняя табличка - это схема модели Post   
ORM нам предоставляет преимущиства абстракции. Мы не только данные для БД описываем  
через классы. К примеру в данном проекте используется БД SQLite3, на продакшене  
будет использоваться другие более продвинутые БД , как postgress, mango DB , Mysql  
итд...
Если бы не ORM, нам бы пришлось вручную писать специфичные запросы под диалект БД.  
Однако, с помощью ORM нам достаточно подключить нашу БД и все запросы будут работать  
без исключения в общем виде.  

Далее,  
Для того, что бы создать модель Post переходим в *models.py* приложения Blog.  
```Python
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
```
В этой моделе постов, создается табличка Post, в которой мы определяем поля:  
```Python
title = models.CharField(max_length=150, db_index=True)
```
В проекте условно будет заголовок постов - *title*  
Он будет экземпляром класса *CharField*, у него есть обязательный элемент  
*max_length=150*   
*db_index=True* - индексация для более быстрого поиска. 

```Python
title = models.SlugField(max_length=150, unique=True)
```
У модели Пост будет *Slug*, который будет использоваться к качесве ЧПУ - человеко  
подобного урла.  

*models.SlugField* - это тоже самое что и *CharField*, только позволяет использовать  
цифры, буквы в обоих регистрах, нижние подчеркивания и дефисы, все остольные  
символы *SlugField* запрещает использовать. *SlugField* это валидатор.  
*unique=True* - уникальные названия.  
```Python
body = models.TextField(blank=True, db_index=True)
```
*blank=True* означает, что поле может быть пустым.   
*db_index=True* - индексация для более быстрого поиска.  

Еще добавим дату публикации постов:
```Python
date_pub = models.DateTimeField(auto_now_add=True)
```
*auto_now_add=True* дата обьекта будет создаваться при сохранении в БД.  

Ниже укажем специальный метод:
```Python
def __str__(self):
    return '{}'.format(self.title)
```
__str__ это метод класса, который возвращает строку.  
Сделано это для того, что бы название класса было такое, как мы укажем в title.  


Далее, необходимо обновить миграции в БД, так как у нас появились изменения в моделях,  но БД пустая.
```bash
/mnt/c/Dev/Blog_Django_Practice_1$ cd BlogEngine/
./manage.py makemigrations
./manage.py migrate
```
Далее, внутри shell, можно создать пост для проверки.  
```bash
 ./manage.py shell
```
```shell
from Blog.models import Post
p = Post(title='New post', slug='new-slug', body='new post body')
>>> p
<Post: New post>
p.save()
```
Мы сохранили обькет в таблице Post.  
Джанго при создании модели прибавляет "менеджера", они находятся в атрибуте   
objects. Если набрать команду dir(p), можно увидеть этот атрибут вместе с другими  
атрибутами класса. 
Все операции сохраниния, изменения, осуществляется через них.  
Теперь создадим пост через "менеджера" моделей:  
```bash
p1 = Post.objects.create(title='new post2', slug='new post2', body='body')
```
Таким образом, вызывать метод *save()* необязательно.  
Что бы посмотреть все обьекты, можно вызвать метод *All()*
```bash
>>> Post.objects.all()
<QuerySet [<Post: New post>, <Post: new post2>]>
```
Еще парочку методов:  
```bash
post = Post.objects.get(slug__iexact='New-slug')
>>> post
<Post: New post>
```
iexact - регистро независимый поиск, который вернет обьект из таблицы Post, у   
которого slug = new-slug ( не чуствителен к регистру )
```bash
post = Post.objects.filter(slug__contains='new')
>>> post
<QuerySet [<Post: New post>, <Post: new post2>]>
```
Есть еще метод - filter, который вернет все записи обьектов в Post, у которых  
slug = new  

**Полный перечень лукапов в документации Django**

Создадим еще 3 поста:  
```bash
>>> p1 = Post.objects.create(title='new post3', slug='new post3', body='body')
>>> p1 = Post.objects.create(title='new post4', slug='new post4', body='body')
>>> p1 = Post.objects.create(title='new post5', slug='new post5', body='body')
```
Теперь все тесты в консоли перенесем во *views.py* нашего проекта. 
```python
from django.shortcuts import render

from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts}) 
```
Меняем старую переменную *n* на новую *posts*, обращаемся к обьекту Post, перед  
этим импортируем эту модель.  
После, в *html* шаблоне меняем старую переменную *names* на *posts*

Еще немного верстки - добавим поля для наших постов с помощью  
[BootStrap](https://getbootstrap.com/docs/5.2/components/card/)   
*index.html* в папке Blog
```html
<div class="card">
  <div class="card-header">
    Featured
  </div>
  <div class="card-body">
    <h5 class="card-title">Special title treatment</h5>
    <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
```
Берем этот кусок кода, и впрыскиваем в него ответ из БД в *index.html* файле нашего приложения:   
```html
 {% block content %}
    <h1 class="mb-5">Posts:</h1>
    {% for post in posts %}

    <div class="card mb-4">
        <div class="card-header">
          {{ post.date_pub}}      <!-- Дата публикации -->
        </div>
        <div class="card-body">
          <h5 class="card-title">{{ post.title }}</h5>  <!-- Названиве поста --> 
          <p class="card-text">{{ post.body|truncatewords:15 }}</p> <!-- содержание поста , с ограничением в 15 символов -->
          <a href="#" class="btn btn-light">Read</a> <!-- пока что неактивная кнопка -->
        </div>
      </div>
    {% endfor %}
{% endblock %}
```
Проверяем в браузере результат.  
Теперь можно добавить ссылку из Navbar  
Переходим в корневой *base.html* папке templates:  

Ищем где начинается кнопка Home и меняем на этот код, который надо донастроить:  
```html
<li class="nav-item">
                <a class="nav-link active" aria-current="page" href="{% url 'posts_list_url' %}">Blog</a>
              </li>
```
Тут в **href** добавили конструкцию *{% url 'posts_list_url' %}*, что это такое?
Во первых, надо добавить в нашу функцию *include* в *urls.py* 3-ий аргумент, а именно имя.  
```python
from django.urls import path

from .views import *


urlpatterns = [
    path('', posts_list, name='posts_list_url')
]
```
И получается что мы используем url ссылку внутри джанги, которую в ставляем в джанговое выражение {% %}
Теперь если проверить в браузере, при нажатии на Home, нас перенаправляет на страницу постов.  

Далее по проекту.. Необходимо добавить страничку детализации постов, для того, что бы можно было зайти в конкретный пост и прочитать его. Причем, ссылка для   
странички конкретного поста имеет человеческий вид, это как раз и есть slug,  
который заполнялся в нашей модели постов. К тому же sLug созадвался как уникльный.  

Допишем в наши урлы новый путь:  
```Python
urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', post_detail, name='post_detai_url')
]
```
Затем необходимо добавить новую функцию *post_Detail*, которая еще не существует в папке *views.py* приложения Blog:  
```Python
def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post': post})
```
В ней мы создаем переменную, где обращаемся к объекту Post, на подобии как было в Shell, когда создавали сами посты. С помощью метода *slug__iexact* мы обращаемся к регистронезависимому компоненту slug, и его рендерим в еще пока    несозданном *post_detail.html* шаблоне.   

Далее создаем *post_detail.html* файл в шаблонах приложения блог:  
```html
{% extend 'Blog/base_blog.html %}

{% block title %}
    {{ post.title }} - {{}}
{% endblock %}
```



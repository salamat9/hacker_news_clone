<h1>Тестовое задание: клон <a href="https://news.ycombinator.com/">Hacker news</a></h1>
<hr>

<p>Что бы запустить проект локально стяните репозиторий:</p>

> git clone git@github.com:salamat9/hacker_news_clone.git`

<p>после перейдите в папку hacker_news_clone</p>

> cd hacker_news_clone

<hr>
<h3>запуск с помощью докера</h3>

<p>создайте образ</p>

> docker-compose up -d build

<p>примените миграции</p>

> docker-compose exec web python manage.py migrate

<p>создайте супер пользователя и запустите проект</p>

> docker-compose exec web python manage.py createsuperuser
> docker-compose exec web python manage.py runserver
> документация эндпоинтов:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/82950d9a4113a86843bb?action=collection%2Fimport)

<hr>







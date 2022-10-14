# Alternative_Flask_Blog
Полноценный блог на Flask, в котором можно добавлять статьи и читать статьи других людей.
В проекте вместе с Flask применяются: Flask-SQLAlchemy, Flask-WTF, Flask-Login и другие библиотеки.

Сайт поддерживает регистрацию и авторизацию пользователей, имеет форму обратной связи и поиска статей по ключевым словам. На главной странице можно разместить рекламу различных статей, я в данном случае разместил ссылки на другие свои проекты.

## Запуск проекта
* Версия python 3.10.7
* Клонируем репозиторий себе в виртуальное окружение `git clone https://github.com/NiatpacBlack/Alternative_Flask_Blog.git`
* Переходим в папку проекта `cd Alternative_Flask_Blog `
* Устанавливаем зависимости из requirements.txt: `pip install -r requirements.txt` 
* вводим команду: `flask run` для запуска приложения
* альтернативный вариант для Unix-систем - установите gunicorn `pip3 install gunicorn` и введите команду `gunicorn --bind 127.0.0.1:5000 app:app`, в данном случае приложение будет доступно в локальной сети.
* aльтернативный вариант для Windows - установите waitress `pip install waitress` и введите команду `waitress-serve --listen=127.0.0.1:5000 app:app`
## Превью сайта
![Peek 2022-10-14 04-52](https://user-images.githubusercontent.com/84034483/195747971-769ff745-84eb-46b9-bb2d-288304105b5f.gif)

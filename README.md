# Проект Пароли и компании (Django REST framework)
________
API приложения для записи поролей и название компаний.<br>
Приложение построенно на REST приложение, взаимодействие через API 


Данный проект написан не фрейморке Django REST framework, с подключением реляционной базы данных "PostgreSQL"<br>
Ипользовалось вирутальное окружение ```venv```
В  проекте построенно 2 модели БД:
1. Таблица "User";
2. Таблица "PasswordCompany" прямая связь с моделью User;

# О проекте
В проекте Описан CRUD для модели PasswordCompany.<br> 
Для реализации CRUD для User использутся Viewsets, а для PasswordCompany - Generic-классы. <br>
Для работы с приложением использовалась программа "Postman".<br>
Приложение покрыто тестами, используется встроенная библиотек 'unittest' (APITestCase).<br>
Суть приложения проста:<br>
Любой зарегистрировавшиеся пользователь, может добавлять сайт(компанию) и пароли для доступа на эти сайты.<br>
Пользователи не могут просматривать пароли и сайты(компании), других пользователей. Пользователю видны только свои пароли и свои сайты.<br>
Просматривать все пароли и сайты, может только менеджер,(в папке 'fixtures' лежит фикстура с группой на менеджера).<br>
Так если пользователь не зарегестрировался, он не сможет добовлять ничего в приложение. Доступ получают для создание записей только те пользователи, которые прошли регистрацию.<br>
После того, как вы добавили пользователя, необходимо пройти по адресу "users/token/", чтобы забрать токен, этот токен необходимо вводить в Headers, в формате ```Bearer дальше токен```.<br>
Команда для создания группы 'manager', в админ панели:
```
python manage.py loaddata fixtures/groups.json
```
Для запуска проекта необходимо сделать.
1. git clone репозитория
```
git@github.com:Meatdam/Password_Company_API.git
```
2. Установить виртуальное окружение `venv`
```
python3 -m venv venv для MacOS и Linux систем
python -m venv venv для windows
```
3. Активировать виртуальное окружение
```
source venv/bin/activate для MasOs и Linux систем
venv\Scripts\activate.bat для windows
```
4. установить файл с зависимостями
```
pip install -r requirements.txt
```
4. Создать базу данных в ```PgAdmin```, либо через терминал. Необходимо дать название в файле settings.py в каталоге 'base' в константе (словаре) 'DATABASES'

5. Создать файл .env в корне проекта и заполнить следующие данные:
```
SECRET_KEY=
DEBUG=

# DB settings
POSGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
DJANGO_SETTINGS_MODULE=

ADMIN_EMAIL=

```
Или выполнить команду ``` docker compose up``` для создания докер контейнера, но не забывайте прописать данные в файле .env с своими данными.
Автор проекта:<br>
[Кузькин Илья](https://github.com/Meatdam)

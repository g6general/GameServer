## Макет игрового сервера

Используется стек технологий: HTML/JS/Python/Django/MySQL/C++

Требуемые компоненты:
* Python 3.7.0
* MySQL 8.0.12
* CMake 3.13.1

### Установка и запуск (for macOS and linux)  

1. Клонирование репозитория  
`$ git clone https://github.com/g6general/Server.git` (https)    
`$ git clone git@github.com:g6general/Server.git` (ssh)

2. Создание виртуального окружения (optional)   
`$ cd ./Server`  
`$ python3 -m vena virt` (название "virt" указано в .gitignore)  
`$ source ./virt/bin/activate` (вход)  
`$ deactivate` (выход)  
3. Установка зависимостей  
`(virt)$ pip install -r ./requirements.txt`
4. Сборка ядра  
`$ cd ./Core/Build`  
`$ cmake ..`  
`$ make`  
`$ cd ../..`   
5. Создание базы данных и пользователя (только при 1-ом клонировании)  
`$ mysql -u root -p`  
`mysql> CREATE DATABASE accounts DEFAULT CHARACTER SET utf8;`  
`mysql> CREATE USER 'django_user'@'localhost' IDENTIFIED BY 'django_passwd';`   
`mysql> GRANT ALL PRIVILEGES ON accounts.* TO 'django_user'@'localhost';`  
`mysql> FLUSH PRIVILEGES;`  
`mysql> exit;` 
6. Миграции и синхронизация с базой данных   
`(virt)$ python ./manage.py makemigrations`  
`(virt)$ python ./manage.py migrate --run-syncdb`
7. Создание пользователя для админки Django (только при 1-ом клонировании)  
`(virt)$ python ./manage.py createsuperuser`  
`(virt)$ Username: <user_name>`  
`(virt)$ Email address: <email_adress>`  
`(virt)$ Password: <password>`  
`(virt)$ Password (again): <password>`  
8. Запуск сервера    
`(virt)$ python ./manage.py runserver` (сервер MySQL должен быть запущен)

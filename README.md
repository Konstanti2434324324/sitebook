# sitebook
Сайт с книгами, которое позволит пользователям создавать собственную цифровую библиотеку: добавлять книги, управлять коллекцией и скачивать литературу.  
## Реализованный функционал  
Регистрация новых пользователей  
Авторизация пользователей  
Выход из системы  
  
## Контроль доступа  
Ограничен доступ к части страниц дня незарегистрированных пользователей, реализовано перенаправление на страницу регистрации.  
  
## Инфраструктура  
База данных PostgreSQL  
Статические файлы - CSS, HTML  
Маршрутизация - четкая структура URL и переходов между страницами  
  
## Технологический стек  
Backend: Python, Django  
База данных: PostgreSQL  
Фронтенд: HTML, CSS  
  
## Запуск   
git clone https://github.com/Konstanti2434324324/sitebook  
cd sitebook  
python -m venv venv  
venv\Scripts\activate   
pip install -r requirements.txt  
createdb sitebook_db  
python manage.py migrate  
python app.py db upgrade  
python manage.py runserver  

![Image](https://github.com/user-attachments/assets/d320a5cc-eaf0-4aeb-9a4d-ddb8dd0d086d)

![Image](https://github.com/user-attachments/assets/a57ff1b7-fb0d-4c9a-9e69-f6bbc5f6c647)

![Image](https://github.com/user-attachments/assets/458e0926-accd-4e3d-8c49-7336fe751417)

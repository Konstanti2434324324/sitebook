from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render




menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
]



data_db = [
    {'id': 1, 'title': 'Сестра Керри', 'author': 'Теодор Драйзер', 'in_stock': True},
    {'id': 2, 'title': 'Финансист', 'author': 'Теодор Драйзер', 'in_stock': True},
    {'id': 3, 'title': 'Три товарища', 'author': 'Эрих Мария Ремарк', 'in_stock': True},
]

cats_db = [{'id': 1, 'name': 'Художественная литература'},
           {'id': 2, 'name': 'Научная литература'},
           {'id': 3, 'name': 'Учебная литература'},
]


def index(request):
    # t = render_to_string('book/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'book/index.html', context=data)
@login_required
def about(request):
    return render(request, 'book/about.html', {'title': 'О сайте', 'menu': menu})

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')



from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import TemplateView
from .models import *
from decimal import Decimal


def read_from_games():
    a = Game.objects.values('title','description', 'cost')
    context = []
    for i in a:
        formatted_string = f"{i['title']}| {i['description']}. Cтоимость: {i['cost']}"
        context.append(formatted_string)
    return  context

# Create your views here.

def index(request):
    title = "Магазин футболок"
    head = "Главная страница"
    context = {
        'title' : title,
        'head': head,
    }
    return render(request, 'head.html', context)

def shop(request):
    shop = " Магазин "
    menu_shop = ' Игры  '
    #catalog = ['Футболка с начесом', 'Футболка с принтом', 'Футболка обычная']
    catalog = read_from_games()
    context = {
        'shop': shop,
        'menu_shop': menu_shop,
        'catalog':  catalog
    }
    return render(request, 'shop.html', context)

def basket(request):
    return render(request, 'basket.html')

def control(username, pass_, pass_ret, age,users):
    info = {}
    if username in users:
        info = "Пользователь уже существует"
        return  info
    elif pass_ != pass_ret:
        info = "Пароли не совпадают"
        return  info
    elif age < 18:
        info = "Вы должны быть старше 18"
        return  info

    info =  f'Приветствуем {username}'
    return  info

def index(request):
    return render(request, 'index.html')


def sign_up_by_html(request):
    #users=["первый","второй", "третий"]
    users= Buyer.objects.values_list('name',flat=True)

    info ={}
    if request.method == 'POST':
        username = request.POST.get('username')
        pass_ = request.POST.get('pass_')
        pass_ret = request.POST.get('pass_ret')
        age = int(request.POST.get('age'))
        str = control(username, pass_, pass_ret, age, users)
        info = {"error": str}
        if str.find('Приветствуем') != -1:
            new_user = Buyer.objects.create(name = username, age = age, balance = 1000)
            new_user.save()

        return render(request, 'registration_page.html',info)
    info = {}
    return render(request, 'registration_page.html', info)


from .forms import ContactForm
def sign_up_by_django(request):
    users= Buyer.objects.values_list('name',flat=True)
    info = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pass_ = form.cleaned_data['pass_']
            pass_ret = form.cleaned_data['pass_ret']
            age = int(form.cleaned_data['age'])
            str = control(username, pass_, pass_ret, age, users)
            info = {"error": str}
            if str.find('Приветствуем') != -1:
                new_user = Buyer.objects.create(name=username, age=age, balance=1000)
                new_user.save()
            return render(request, 'registration_page.html', info)
    else:
        form = ContactForm()
    return render(request,'registration_page.html', {'form': form} )

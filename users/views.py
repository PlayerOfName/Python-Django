from django.shortcuts import redirect, render
from users.forms import UserRegisterForm, UserCommentsForm
from django.contrib.auth.decorators import login_required
from users.models import Comments, Profile
from django.contrib.auth.models import User

# Create your views here.

# Вывод страницы регистрации
def register(request):

    username = ''

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

        context = {'form':form, 'username':username}
        return render(request, 'users/home.html', context)
    else:
        form = UserRegisterForm()
    return render(request, 'users/registr.html', {'form':form})

# Вывод главной страницы
def home(request):
    return render(request, 'users/home.html')

# Вывод страницы для игр
def game(request):
    return render(request, 'users/game.html')

# Вывод динозаврика 
def DinoGame(request):
    return render(request, 'users/game/dino-game.html')

# Вывод страницы профиля 
@login_required
def profile(request):

    maxim = -1

    list_profile = User.objects.all()

    for item in list_profile:
        maxim = max(maxim, item.id)

    return render(request, 'users/profile.html', {'max_id':maxim})

# Вывод страницы записи комментариев
def Comment(request):

    if request.method == 'POST':
        form_2 = UserCommentsForm(request.POST)

        if form_2.is_valid():
            form_2.save()

        
    else:
        form_2 = UserCommentsForm()
    return render(request, 'users/komment.html', {'form_2':form_2})

# Вывод страницы просмотра комментариев
def viewComment(request):
    context = Comments.objects.all()

    return render(request, 'users/views_com.html', {'comment':context})

# Вывод страницы змейки
def SnakeGame(request):
    return render(request, 'users/game/snake.html')

# Вывод страницы тетриса
def TetrisGame(request):
    return render(request, 'users/game/tetris.html')

# Вывод страницы с крестиками-ноликами
def XOGame(request):
    return render(request, 'users/game/XO.html')
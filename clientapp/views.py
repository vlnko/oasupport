from django.shortcuts import render, redirect
from .models import Call
from .forms import CallForm, LoginForm
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout


def index(request):
    user = request.user

    if user.is_authenticated:
        calls = Call.objects.filter(author__company=request.user.company).filter(is_archived=False)
        return render(request, 'clientapp/index.html', {'title': 'Главная страница', 'calls': calls, 'user': user})
    else:
        return redirect('login')


def callsarchive(request):
    user = request.user

    if user.is_authenticated:
        calls = Call.objects.order_by('-id').filter(author__company=request.user.company).filter(is_archived=True)
        return render(request, 'clientapp/archive.html', {'title': 'Архив обращений', 'calls': calls})
    else:
            return redirect('login')


def addnewcall(request):
    user = request.user
    
    if user.is_authenticated:
        error = ''
        if request.method == 'POST':
            form = CallForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.author = request.user
                form.save()
                return redirect('home')
            else:
                error = 'Форма была неверной. Попробуйте еще раз.'

        form = CallForm()
        context = {
            'form': form,
            'error': error,
        }

        return render(request, 'clientapp/addnewcall.html', context)
    else:
        return redirect('login')


def LoginView(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form,
    }

    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    else:
        return render(request, 'clientapp/login.html', context)


def LogoutView(request):
    logout(request)
    return redirect('login')


class CallDetailView(DetailView):
    model = Call
    template_name = 'clientapp/call.html'
    context_object_name = 'call'



import random
from django.shortcuts import render
from users_generator.randomengine.random import RandomUserData


def index(request):

    r = RandomUserData()
    user = r.full_random_user()
    context = {
        'user': user
    }
    return render(request, 'users_generator/index.html', context)


def castom_user(request):

    r = RandomUserData()

    if request.method == 'POST':

        data_from = request.POST.get('data_from')
        data_to = request.POST.get('data_to')
        gender = request.POST.get('gender')
        r.start_date = data_from
        r.stop_date = data_to
        r.gender = gender
        user = r.castom_random_user()
        context = {
            'user': user
        }
        return render(request, 'users_generator/castom_user.html', context)
    else:

        user = r.full_random_user()
        context = {
            'user': user
        }
        return render(request, 'users_generator/castom_user.html', context)

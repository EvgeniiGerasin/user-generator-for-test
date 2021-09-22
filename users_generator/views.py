from django.shortcuts import render
from users_generator.randomengine.random import RandomUserData


def index(request):

    r = RandomUserData()
    user = r.full_random()
    context = {
        'user': user
    }
    return render(request, 'users_generator/index.html', context)

import os
from django.shortcuts import render
from users_generator.randomengine.random import RandomUserData
from django.http import HttpResponse
import mimetypes


def index(request):

    r = RandomUserData()
    user = r.full_random_user()
    context = {
        'user': user
    }
    return render(request, 'users_generator/index.html', context)


def castom_user(request):

    try:
        os.remove('users_generator/randomengine/csv/data_users.csv')
    except:
        pass
    r = RandomUserData()

    if request.method == 'POST':

        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        gender = request.POST.get('gender')
        number = int(request.POST.get('number'))
        csv = bool(request.POST.get('type'))
        r.start_date = date_from
        r.stop_date = date_to
        r.gender = gender
        user = r.castom_random_user()
        context = {
            'user': user,
            'date_from': date_from,
            'date_to': date_to,
            'gender': gender,
        }
        if csv:
            r.generate_csv_users(number=number)
            path = open('users_generator/randomengine/csv/data_users.csv', 'r')
            mime_type, _ = mimetypes.guess_type('users_generator/randomengine/csv/data_users.csv')
            response = HttpResponse(path, content_type=mime_type)
            response['Content-Disposition'] = "attachment; filename=%s" % 'data_users.csv'
            return response
        return render(request, 'users_generator/castom_user.html', context)
    else:
        user = r.full_random_user()
        context = {
            'user': user,
            'date_from': '1970-01-01',
            'date_to': '2009-01-01',
            'gender': 'random',
        }
        return render(request, 'users_generator/castom_user.html', context)

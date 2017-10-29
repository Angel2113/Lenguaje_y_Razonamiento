from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from .forms import SeForm

from .models import Busqueda, Tweet
from .sinAPI import *
from .conAPI import *

class Home(View):
    def get(self, request, *args, **kwargs):
        form = SeForm(request.POST or None)
        context = {
            'form': form
        }
        return render(request, 'gris.html', context=context)# Create your views here.

def busqueda(request):
    if request.method == 'POST':
        texto = request.POST.get('busqueda')
        cantidad = request.POST.get('cantidad')
        tipo = request.POST.get('tipo')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        cantidad_elegida  = 1000 if int(cantidad) > 1000 else int(cantidad)


        # Parseo de las cadenas
        for b in texto.split(' '):
            obj = guarda_busqueda(b, cantidad_elegida, tipo, fecha_inicio, fecha_fin)
            if b.startswith('#'):
                print('Es un hash', b)
            elif b.startswith('@'):
                print('Es un usuario', b)
            else:
                print('ninguno de los 2', b)

        return JsonResponse({'texto': texto})

def guarda_busqueda(busqueda, cantidad, tipo, fecha_inicio=None, fecha_fin=None):
    obj = Busqueda(
        busqueda=busqueda,
        tipo=tipo,
        cantidad=cantidad
    )
    obj.save()
    return obj

def search(refeencia):
    pass

'''
        # Busca los datos y los guarda en la base de datos
        if tipo == 'sinAPI':
            if tipo == 'User':
                r = get_by_username(busqueda, cantidad)
                for tweet in r:
                    new_insert = Tweet(
                        busqueda=obj,
                        ide=tweet.id,
                        permalink=tweet.permalink,
                        username=tweet.username,
                        text=tweet.text,
                        date=tweet.date,
                        formatted_date=tweet.formatted_date,
                        retweets=tweet.retweets,
                        favorites=tweet.favorites,
                        mentions=tweet.mentions,
                        hashtags=tweet.hashtags,
                        geo=tweet.geo,
                        urls=tweet.urls,
                        author_id=tweet.author_id
                    )
                    new_insert.save()
            elif tipo == 'Query':
                r = get_by_query(busqueda, cantidad)
                for tweet in r:
                    new_insert = Tweet(
                        busqueda=obj,
                        ide=tweet.id,
                        permalink=tweet.permalink,
                        username=tweet.username,
                        text=tweet.text,
                        date=tweet.date,
                        formatted_date=tweet.formatted_date,
                        retweets=tweet.retweets,
                        favorites=tweet.favorites,
                        mentions=tweet.mentions,
                        hashtags=tweet.hashtags,
                        geo=tweet.geo,
                        urls=tweet.urls,
                        author_id=tweet.author_id
                    )
                    new_insert.save()
        elif llaves == 'conAPI':
            if tipo == 'User':
                r = user_tweets(busqueda)
                s = r[0]
                json_str = json.dumps(s._json)
                print(json_str)
                for tweet in r:
                    new_insert = Tweet(
                        busqueda=obj,
                        ide=tweet.id,
                        username=tweet.user.screen_name,
                        text=tweet.text
                    )
                    new_insert.save()

            elif tipo == 'Query':
                pass
'''


    #text = request.GET.get('comment', None)
    #historia = request.GET.get('historia', None)
    #r = get_Babi(text, historia)

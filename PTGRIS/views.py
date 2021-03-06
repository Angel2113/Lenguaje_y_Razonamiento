from django.shortcuts import render
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from .forms import SeForm

from .models import Busqueda, Tweet
from .sinAPI import *
from .conAPI import *
import json
import csv

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

        ## Guion bajo o buscar un nombre de usuario
        for b in texto.split(' '):
            obj = guarda_busqueda(b, cantidad_elegida, tipo, fecha_inicio, fecha_fin)
            if b.startswith('@'):
                print('Es un usuario', b)
                down_user(b, obj, cantidad_elegida)
            else:
                print('Es una consulta', b)
                print(tipo)
                if(tipo == 'presente'):
                    down_api_tweets()
                if(tipo == 'pasado'):
                    down_all_tweets(b, obj, cantidad_elegida)

        return JsonResponse({'texto': texto})

def guarda_busqueda(busqueda, cantidad, tipo, fecha_inicio=None, fecha_fin=None):
    obj = Busqueda(
        busqueda=busqueda,
        tipo=tipo,
        cantidad=cantidad
    )
    obj.save()
    return obj

def down_user(busqueda, obj, cantidad):
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

def down_all_tweets(busqueda, obj, cantidad):
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

def down_api_tweets(referencia):
    pass


#### despliegue de datos

# Obtiene las busquedas
def get_busquedas(request):
    objects = Busqueda.objects.all().values('folio', 'busqueda', 'cantidad')
    #return JsonResponse(list(objects), safe=False)
    return HttpResponse(json.dumps({'resultado':list(objects)}))


## descargar los datos

# descarga como json
def get_json(request):
    folio = request.POST.get('folio')
    b = Busqueda(folio=folio)

    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="salida.json"'
    #dictionaries = [obj.as_dict() for obj in Tweet.objects.all().filter(busqueda=b).values()]
    output = []
    for d in Tweet.objects.all().filter(busqueda=b).values():
        #response.write(d)
        output.append(d)
    response.write(json.dumps(output))
    return response

# descarga como csv
def get_csv(request):
    folio = request.POST.get('folio')
    b  = Busqueda(folio=folio)

    # Escribe la cabecera del csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tweets.csv"'
    response['Content-Type'] = 'application/x-download'

    writer = csv.writer(response)
    writer.writerow(['ide', 'permalink', 'username', 'text', 'hashtags', 'geo', 'urls', 'author_id'])


    for e in Tweet.objects.all().filter(busqueda=b).values():
        try:
            writer.writerow([e['ide'], e['permalink'], e['username'], e['text'], e['hashtags'], e['geo'], e['urls'], e['author_id']])
        except:
            pass

    return response




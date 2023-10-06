from django.shortcuts import render
import requests
import datetime

def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Amsterdam'    
    appid = '784f5246ba9701c069a9f8bca06dc812'
    URL ='https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city,'appid':appid,'units':'metric'}
    r= requests.get(url=URL,params=PARAMS)
    r.raise_for_status()
    res= r.json()
    description= res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp= res['main']['temp']

    day = datetime.date.today()
    return render(request, 'index.html', {'description':description, 'icon':icon, 'temp':temp,'day':day,'city':city})
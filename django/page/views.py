import logging
from django.shortcuts import render_to_response
from datetime import datetime
from models import Event

logger = logging.getLogger(__name__)

def home(request):
    logger.debug('calling page.views.home()')

    context = {
        'page_title': 'Home',
    }
    return render_to_response('home.html', context)

def detail(request, page_slug):
    
    context = {
        'page_title': page_slug,
    }
    return render_to_response(page_slug +'.html', context)

def schedule(request):
    currentYear = datetime.now().year
    #events = Event.objects.filter(event_date__year=currentYear)
    events = Event.objects.filter(active=True)
    schedule = {}
    i = 1
    for event in events:
        schedule[i] = event
        i += 1

    context = {
        'page_title': 'schedule',
        'currentYear': currentYear,
        'schedule': schedule,
    }
    
    return render_to_response('schedule.html', context)


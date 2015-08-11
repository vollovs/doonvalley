import logging
from django.shortcuts import render_to_response

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


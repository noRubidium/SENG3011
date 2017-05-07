"""
The view layer of the API, handle string beautify and stuff
"""

import datetime

from django.http import HttpResponse, JsonResponse

from .crocs import cross_origin
import urllib2


@cross_origin
def index(request, url):
    """
    # Index route, only echo the request
    :param request: http request
    :param url: url
    :return: http response
    """
    try:
        response = urllib2.urlopen(url)
        html = response.read()
    except Error:
        return HttpResponse('Not Found', status=404)
    return HttpResponse(html)


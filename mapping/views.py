"""
The view layer of the API, handle string beautify and stuff
"""
import json
from django.http import JsonResponse
from .crocs import cross_origin

import urllib2
from .utils import industries, companies, get_pe_private


@cross_origin
def get_company_industries(request, company):
    """
    get the request, return industries the company belongs to
    :param request: http request
    :param company: company string (3 digit only)
    :return: JSON of industries related to company
    """

    response = {'industries': map(lambda x: {'name': x, 'pe_ratio': get_pe_private(x)}, industries[company])}

    return JsonResponse(response)


@cross_origin
def get_industry_companies(request, industry):
    """
    get the request, return companies belonging to the industry
    :param request: http request
    :param company: industry string
    :return: JSON of companies inside industry
    """

    response = {'companies': companies[industry], 'pe': get_pe_private(industry)}

    return JsonResponse(response)


@cross_origin
def get_related_companies(request, company):
    """
    get the request, return industries the company belongs to
    :param request: http request
    :param company: company string (3 digit only)
    :return: JSON of industries related to company
    """

    related_companies = set()
    for i in industries[company]:
        for c in companies[i]:
            if c != company:
                related_companies.add(c)

    related_companies = list(related_companies)
    related_companies.sort()
    response = {'related_companies': related_companies}

    return JsonResponse(response)


@cross_origin
def get_industry_pe_ratio(request, industry):
    response = {'data': get_pe_private(industry)}
    return JsonResponse(response)
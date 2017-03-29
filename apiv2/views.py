from django.http import HttpResponse, JsonResponse
from utils import getCommodityNumber,getCategoryNumber,getStateNumber
from parse import parse_merchandise, parse_retail

# django.json or something...

def index(request):
    return HttpResponse("This is the API end point v2.")


def showMerchandiseData(request, commodities, states="AUS"):
    startDate = request.GET.get('startDate', 'defaultStartDate')
    endDate = request.GET.get('endDate', 'defaultEndDate')

    # init a Merchandise Object (pass in the args needed, look at models.py)
    # get the JSON file with the get_data method or something like that

    # result = parse_merchandise(jsonfile)
    # return JsonResponse(result)

def showRetailData(request, categories, states="AUS"):
    startDate = request.GET.get('startDate', 'defaultStartDate')
    endDate = request.GET.get('endDate', 'defaultEndDate')

    # init a Retail Object (pass in the args needed, look at models.py)
    # get the JSON file with the get_data method or something like that

    # result = parse_commodity(jsonfile)
    # return JsonResponse(result)
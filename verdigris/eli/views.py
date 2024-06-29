from django.http import HttpResponse

from .apps import App

def ping(request):
    return HttpResponse("Success")

def eli_post(request):
    if request.method == 'POST':
        # Param for input csv
        # read the input csv. For each row, call Eli API
        # helpMe()
        App.read_csv("./data/input.csv")

        # update output file
        
        # Return a 204 No Content response
        return HttpResponse(status=200, content="Success")

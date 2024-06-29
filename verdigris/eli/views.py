from django.http import HttpResponse

from .apps import App

def ping(request):
    return HttpResponse("Success")

def eli_post(request):
    if request.method == 'POST':
        # Param for input csv
        # read the input csv. For each row, call Eli API
        # helpMe()
        result = App.read_csv("./data/input.csv")

        # update output file
        App.writeJson(result, "./data/target_customers.json")
        
        # Return a 200 response
        return HttpResponse(status=200, content="Success")

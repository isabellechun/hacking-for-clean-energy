from django.http import HttpResponse

def ping(request):
    return HttpResponse("Success")

def eli_post(request):
    if request.method == 'POST':
        # Param for input csv
        # read the input csv
        # For each row, call Eli API
        # update output file
        
        # Return a 204 No Content response
        return HttpResponse(status=204)

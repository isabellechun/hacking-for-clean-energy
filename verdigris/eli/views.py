from django.http import HttpResponse

def ping(request):
    return HttpResponse("Success")

def eli_post(request):
    if request.method == 'POST':
        # Handle any necessary processing for POST requests here
        
        # Return a 204 No Content response
        return HttpResponse(status=204)

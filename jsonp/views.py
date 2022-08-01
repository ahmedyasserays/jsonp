from django.http.response import HttpResponse

def index(request):
    callback = request.GET.get("callback")
    if callback:
        result = callback + '({"name":"ahme", "age":21})'
    else:
        result = 'func({"name":"ahme", "age":21})'
    return HttpResponse(result, content_type ='application/javascript')
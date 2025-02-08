from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    return render(request, 'home.html')

def submitquery(request):
    q = request.GET['query'] 
    try:
        res=eval(q)
        mydict={
            'q': q,
            'res': res,
            'error': False,
            'result': True,
        }
        return render(request, 'home.html')
    except: 
        mydict={
            'error': True,
            'result': False,
        }
        return render(request, 'home.html', context=mydict)
    
def page_not_found_error(request, exception):
    return render(request, 'calculator/404.html', status=404)
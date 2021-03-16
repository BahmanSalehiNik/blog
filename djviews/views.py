from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

'''
def home(request):
    #print(dir(request))
    print(request.method)
    #print(request.COOKIES)
    print(request.headers)
    print(request.user)
    print(request.get_full_path())
    return HttpResponse("<!DOCTYPE><html><style>h1{color: blue}</style><h1>Hello<h1></html>")

'''''


def home(request):
    response = HttpResponse(content_type='application/json')
    response.write('<p>Test!</p>')
    response.write('<style>h1{color: blue}</style><p>Test!</p>')
    return response


def redir(request):
    return HttpResponseRedirect('http://www.google.com')
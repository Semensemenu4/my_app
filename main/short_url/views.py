from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index( request ):
    return HttpResponse( '<h1> MAIN </h1>' )

def pageNotFound( request, exception ):
    return HttpResponseNotFound( '<h1> 404 </h1>' )

from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render




def index(request) :
    now = datetime.now()
    #html_content = "<html><head><title>Helloworld, Django</title></head><body>"
    #html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A, %d %B, %Y at %X")
    #html_content += "</body></html>"

    return render(
        request,
        "HelloworldDjangoApp/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'title' : "Helloworld Django App", 
            'massage' : "Helloworld Django",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def about(request) :
    return render(
        request,
        "HelloworldDjangoApp/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )
 
# Create your views here.

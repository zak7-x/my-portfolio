from django.shortcuts import render

def index(request):
    # Show the homepage.
    return render(request, "home.html")

def about(request):
    # Show the About Me page.
    return render(request, "about/about.html")

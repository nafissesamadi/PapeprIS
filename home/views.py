from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request, 'home/index_page.html')


def header_component(request):
    context={'link':'Q1 Papers'}
    return render (request, 'shared/header.html',context)

def footer_component(request):
    return render (request, 'shared/footer.html',{})
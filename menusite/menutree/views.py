from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Menu
from django.template import loader
from django.shortcuts import render, get_object_or_404


def index(request):
    return HttpResponse("Hello, world. You're at the menutree index.")

def mainmenu(request, id):
    # try:
    #     menu = Menu.objects.get(id=id)
    # except Menu.DoesNotExist:
    #     raise Http404("Менюшки с таким индексом не существует")
    # menu = get_object_or_404(Menu, pk=id)
    context = {
        "id": id,
        # "menu": menu,
        "menu_list": [menu.id for menu in Menu.objects.all()],
        "menu_list1": [menu for menu in Menu.objects.all()],
        "request": request,
    }
    return render(request, "menutree/index.html", context)

from django import template
from menutree.models import *
from menutree.views import *

register = template.Library()

@register.simple_tag(name='menu')
def get_menu(filter=None):
    if not filter:
        return Menu.objects.all()
    else:
        return Menu.objects.filter(pk=filter)

@register.simple_tag(name='menu_id')
def get_menu_id(filter=None):
    if not filter:
        return [menu.id for menu in Menu.objects.all()]
    else:
        return Menu.objects.filter(pk=filter)

@register.simple_tag(name='main_menu')
def get_main_menu():
    for menu in Menu.objects.all():
        if menu.mother_menu == None:
            return menu

@register.simple_tag(name='all_way')
def get_all_way(id):
    way_list = []
    daughter = Menu.objects.filter(pk=id)[0]
    way_list.append(daughter.id)
    while daughter.mother_menu != None:
        id = daughter.mother_menu.id
        daughter = Menu.objects.filter(pk=id)[0]
        way_list.append(daughter.id)

    return way_list[::-1]

@register.simple_tag(name='get_ways')
def get_ways(id):
    list_ways = []
    # parrent = [m for m in Menu.objects.filter(mother_menu=id)]
    # # ways_list.append(parrent)
    # print(parrent)
    # while id != None:
    #     if Menu.objects.filter(id=id)[0].mother_menu == None:
    #         break
    #     id = Menu.objects.filter(id=id)[0].mother_menu.id
    #     parrent = [m for m in Menu.objects.filter(mother_menu=id)]
    #     print(parrent)
    def get_ways_recursion(id, daughter=None, arr=None, id_way=None):
        ways = get_all_way(id_way)
        if id_way == 1:
            for m in Menu.objects.filter(pk=id_way):
                arr.append(m)
                for d in Menu.objects.filter(mother_menu=m):
                    arr.append(d)
                return arr


        for m in Menu.objects.filter(name_menu=daughter):
            if m.id == 1:
                arr.append(m)
                print(m)
            if id == id_way:
                print('---')
                for d in Menu.objects.filter(mother_menu=daughter):
                    print('***')
                    arr.append(d)
                    print(d)
            elif m.id in ways:
                for d in Menu.objects.filter(mother_menu=m):
                    arr.append(d)
                    print(d)

                for d in Menu.objects.filter(mother_menu=m):
                    if d.id in ways:
                        get_ways_recursion(d.id, d, arr, id_way)
            # elif daughter == 1:
            #     print(m)
        return arr
    # return id
    return get_ways_recursion(1, 'Главное меню', list_ways, id)
    # for m in Menu.objects.filter(mother_menu=1):
    #     for d in Menu.objects.filter(mother_menu=m):
    #         print(d)






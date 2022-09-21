from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    context = {
        'list_movie' : data_mywatchlist,
        'nama' : 'Bella'
    }
    return render(request, 'mywatchlist.html', context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    data_mywatchlist = MyWatchList.objects.all()
    count_true = 0
    count_false = 0
    display_message = ""
    for i in data_mywatchlist:
        if i.watched == True:
            count_true += 1
        else:
            count_false += 1

    if count_true >= count_false:
        display_message = "Selamat, kamu sudah banyak menonton!" 
    else:
        display_message = "Wah, kamu masih sedikit menonton!"

    context = {
        'list_movie' : data_mywatchlist,
        'nama' : 'Bella',
        'display_message' : display_message
    }
    return render(request, 'mywatchlist.html', context)


def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

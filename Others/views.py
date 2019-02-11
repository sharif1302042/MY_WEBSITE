from django.shortcuts import render

def OthersHome(request):
    return render(request,'OthHome.html')


def github1(request):
    return render(request,'github1.html')

def github2(request):
    return render(request,'github2.html')

def Avro(request):
    return render(request,'Avro.html')

def Host_project(request):
    return render(request,'Host_project.html')
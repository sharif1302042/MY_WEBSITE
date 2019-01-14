from django.shortcuts import render


def DjangoHome(request):
    return render(request,'Home.html')
def ORM(request):
    return render(request,'ORM.html')
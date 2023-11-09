from django.shortcuts import render

# Create your views here.

def page_1(request):
    return render(request,'page_1.html')
def page_2(request):
    return render(request,'page_2.html')
def page_3(request):
    return render(request,'page_3.html')
def page_4(request):
    return render(request,'page_4.html')


from django.shortcuts import render

# Create your views here.
def send_data(request):
    d={'name':'naresh'}
    return render(request,'send_data.html',context=d)
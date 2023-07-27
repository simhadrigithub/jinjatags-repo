from django.shortcuts import render

# Create your views here.
d={'name':"simha" , 'age':21, 'habbies':'watching movies','intrest':'python learning'}
def render1(request):
    return render(request,'render1.html',context=d)
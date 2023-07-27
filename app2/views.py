from django.shortcuts import render

# Create your views here.

d={'name':'simha','age':21,'range':100,'frame_work':'django','time':10.35,'from':'chittoor'}

def render2(request):
    return render(request,'render2.html',context=d)

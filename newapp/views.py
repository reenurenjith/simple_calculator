from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def index(request):
##    return HttpResponse("Welcome...!!!!!!")
    html = "<html><body style=background-color:lightgrey><h1 style=text-align:center>SIMPLE ONLINE CALCULATOR<h1><form oninput=m.value=parseInt(a.value)+parseInt(b.value),n.value=parseInt(a.value)-parseInt(b.value),p.value=parseInt(a.value)*parseInt(b.value),q.value=parseInt(a.value)/parseInt(b.value),r.value=parseInt(a.value)%parseInt(b.value)><br>Enter number a :<br><input type=text name=numa id=a ><br>Enter number b :<br><input type=text name=numb id=b > <br> <br> <i> A + B  <var> = <var> <output name=m for=a b></output> <br> A - B<var> = </var> <output name=n for= a b></output> <br> A * B <var> = </var> <output name=p for= a b></output> <br> A / B <var> = </var> <output name=q for= a b></output> <br> A % B <var> = </var> <output name=r for= a b></output> </i> </body></html>"
    return HttpResponse(html)


def detail(request, n):

    return HttpResponse("You're looking at question %s." % n)
    now = datetime.datetime.now()

def results(request, n):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % n)

def vote(request, n):
    return HttpResponse("You're voting on question %s." % n)




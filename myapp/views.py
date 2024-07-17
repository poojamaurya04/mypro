from django.shortcuts import render
from myapp.models import pooja

# Create your views here.
def index(request):
    return render(request,"index.html")
def send(request):
    if request.method=='POST':
        ID=request.POST['ID']
        FULL_NAME=request.POST['FULL_NAME']
        EMAIL_ADDRESS=request.POST['EMAIL_ADDRESS']
        MOBILE_NUMBER=request.POST['MOBILE_NUMBER']
        DOB=request.POST['DOB']
        ADDRESS=request.POST['ADDRESS']
        pooja(ID=ID,FULL_NAME=FULL_NAME,EMAIL_ADDRESS=EMAIL_ADDRESS,MOBILE_NUMBER=MOBILE_NUMBER,DOB=DOB,ADDRESS=ADDRESS).save()
        sms=""
    return render(request,"index.html" ,{'sms':sms})

def showrecord(request):
    data=pooja.objects.all()
    return render(request,"showrecord.html",{'data':data})

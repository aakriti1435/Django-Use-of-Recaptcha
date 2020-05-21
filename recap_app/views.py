from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.

def index(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)

        #recaptcha backend
        clientKey = request.POST['g-recaptcha-response']
        secretKey = 'Enter Your secret key here'

        captchaData = {
            'secret' : secretKey,
            'response' : clientKey
        }
        #API URL
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data = captchaData)
        response = json.loads(r.text)
        verify = response['success']
        print('your success is ', verify)
        if verify:
            return HttpResponse('<script> alert("success");</script>')
        else:
            return HttpResponse('<script> alert("Not success"); </script>')

    return render(request, 'homepage.html')
   

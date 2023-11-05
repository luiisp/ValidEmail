from django.shortcuts import render
from django.views import View

def email_sintaxe(email):
    if not '@' in email or len(email) > 64  or not '.' in email:
        return False
    
    
def send_email(email):
    return 'oi'



class Menu(View):
    def get(self,request):
        notice = None
        stage = 1
        return render(request, 'menu/index.html',{'notice':notice,
                                                  'stage':stage})
    def post(self,request):
        email = request.POST.get('email')
        emailV = email_sintaxe(email)
        if emailV == False:
            notice = 'Email Invalido!'
        else:
            notice = f'Um código verificação foi enviado para {email}'
            stage = 2

        return render(request, 'menu/index.html',{'notice':notice,
                                                  'stage':stage})
       

    


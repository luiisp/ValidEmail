from django.shortcuts import render
from django.views import View
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

def email_sintaxe(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        return True
    else:
        return False
    

def send_email(receiver):
    #SMTP CONFIGS
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'luiisp.validmail@gmail.com'
    smtp_password = 'meru jrih sesu szzo'
    sender = 'Valid Email?'


    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = '🧐 Seu email é valido? - ValidEmail || Github.com/Luiisp'

    email = f"""
    <!DOCTYPE html>
    <html>
    <head></head>
    <body style="margin: 0; padding: 0; background-color: #0A0915; font-family: 'Poppins', sans-serif; text-align: center; color: #fff;">
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
                <td align="center">
                    <div style="width: 100%; max-width: 600px; margin: 0 auto; padding: 20px;">
                    <a href="https://github.com/luiisp/ValidEmail"><img src="https://i.ibb.co/2cLYs1V/520logo.png" alt="logo" style="width: 160px;"></a>
                        <h1 style="color: #4611E5;">Olá {receiver} 👋</h1>
                        <p style="font-size: 14px;">Você acaba de testar minha aplicação DJANGO para verificar se seu email é válido.</p>
                        <p style="font-size: 24px;">Seu código de verificação é:</p>
                        <h1 style="color: #E5115B; font-size: 15vh;">24552</h1>
                        <p style="font-size: 14px;">Insira este código no site que provavelmente deve estar rodando <a href="http://127.0.0.1:8000/" style="color: #11e594; text-decoration: none;">nesta porta</a></p>
                        <p style="font-size: 14px;"><a href="https://github.com/luiisp/ValidEmail" style="color: #4611E5; text-decoration: none;">Visite o repositório oficial</a></p>
                        <a style="color: #ffffff; font-size: 24px;" href="https://github.com/luiisp">GitHub</a>
                        <a style="color: #ffffff; font-size: 24px;" href="https://www.linkedin.com/in/pedro-luis-dias-757225285/">LinkedIn</a>
                    </div>
                </td>
            </tr>
        </table>
    </body>
    </html>

    """
    msg.attach(MIMEText(email, 'html'))
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        txt_email = msg.as_string()
        server.sendmail(sender, receiver, txt_email)
        server.quit()
        return True
    except Exception as e:
        print('Erro ao enviar o email: ' + str(e))
        return False




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
       

    


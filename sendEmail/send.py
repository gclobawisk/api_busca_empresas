import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import codecs
from env_config import *

class EmailSender:
    def __init__(self, name, recipient_email):
        self.name = name
        self.recipient_email = recipient_email


    def send_email_users_list(self):
        # Configurar as informações do servidor de e-mail
        smtp_server = 'smtp.office365.com'
        smtp_port = 587
        smtp_username = 'gabriel.clobawisk@hotmail.com'
        smtp_password = 'gabrieleingryd06'
        smtp_encryption = "tls"
        
        # Configurar o remetente, destinatário e assunto do e-mail
        from_email = 'gabriel.clobawisk@hotmail.com'
        to_email = self.recipient_email
        subject = 'Parabéns 50000 Giros recebidos'

        # Ler o template HTML e substituir o valor da variável "nome"
        with codecs.open('templates/btg_template.html', 'r', encoding='utf-8') as file:
            html = file.read()
            name = self.name
            recipient_email = self.recipient_email
            html = html.format(name=name, recipient_email= recipient_email)

        # Criar a mensagem de e-mail
        msg = MIMEMultipart('related')
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Adicionar o conteúdo HTML à mensagem
        body = MIMEText(html, 'html')
        msg.attach(body)

        # Configurar o servidor SMTP e enviar o e-mail
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            print(f"E-mail enviado com sucesso para {recipient_email}")
        except Exception as e:
            print("Ocorreu um erro ao enviar o e-mail:", e)



from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import json


class MessageMail:
    def __init__(self, subject, html_message, receiver_mail):
        credentials_file = open("automations/credentials.json", "r")
        data_credentials_file = json.load(credentials_file)
        self.email = data_credentials_file["email"]
        self.password = data_credentials_file["password"]
        self.smtp_server = data_credentials_file["smtp_server"]
        self.smtp_port = data_credentials_file["smtp_port"]

        # Assunto do email
        self.email_subject = subject
        # Email que irá receber a msg
        self.receiver_mail = receiver_mail
        # mensagem html enviada no corpo do email
        self.html_message = html_message

        # Close Credentials.json file
        credentials_file.close()

    def send_email(self):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = self.receiver_mail
        msg['Subject'] = self.email_subject
        html_message = self.html_message

        # Body Message ###########################################
        msg.attach(MIMEText(html_message, 'html', 'utf-8'))

        # Attach Image ###########################################
        '''
        # This open assumes the image is in the current directory
        fp = open('verification_flyer_ver1.jpg', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image1>')
        msg.attach(msgImage)
        '''
        # Body Message ###########################################

        email_text = msg.as_string()
        self.smtp_connection.sendmail(self.email, self.receiver_mail, email_text)

    def smtp_connect(self):
        try:
            self.smtp_connection = smtplib.SMTP(self.smtp_server, self.smtp_port)
            self.smtp_connection.set_debuglevel(2)
            self.smtp_connection.starttls()
            self.smtp_connection.login(self.email, self.password)
            print("Connected.")
            print("Email enviado com sucesso")
        except Exception as e:
            print(e)
            print("Ocorreu um erro durante o envio do email")
        return


def mail_form(subject, html_message, receiver_mail):
    message_mail = MessageMail(subject, html_message, receiver_mail)
    message_mail.smtp_connect()
    message_mail.send_email()


def schedule_confirmation(data):
    nome = data['nome']
    receiver_mail = data['email']

    subject = 'Confirmação de agendamento de serviços - Mônaco Peças e Acessórios'
    html_message = """
    <p>Olá, {nome}.</p>
    <p>Estamos passando aqui para avisar que seu agendamento foi confimado.</p>
    <p>Agradecemos por confiar no nosso trabalho.</p>
    """.format(nome=nome)

    mail_form(subject, html_message, receiver_mail)


def finished_service(data):
    nome = data['nome']
    receiver_mail = data['email']

    subject = 'Serviço realizado - Mônaco Peças e Acessórios'
    html_message = """
    <p>Olá, {nome}.</p>
    <p>Estamos passando aqui para avisar que os serviços solicitados foram realizados.</p>
    <p>Seu veículo está disponível para retirada, ou caso tenha sido solicitado, será entregue no endereço informado.</p>
    <p>Agradecemos por confiar no nosso trabalho.</p>
    """.format(nome=nome)

    mail_form(subject, html_message, receiver_mail)

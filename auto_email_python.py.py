import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, corpo):
    remetente = 'seu_email@gmail.com'
    senha = 'sua_senha'

    # Criação do objeto MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Adiciona o corpo ao e-mail
    msg.attach(MIMEText(corpo, 'plain'))

    # Conectar ao servidor SMTP do Gmail
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remetente, senha)
        
        # Enviar o e-mail
        texto = msg.as_string()
        servidor.sendmail(remetente, destinatario, texto)
        servidor.quit()
        
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')

# Uso da função
destinatario = 'destinatario@example.com'
assunto = 'Assunto do E-mail'
corpo = 'Este é o corpo do e-mail. Pode incluir a frase e o texto que você desejar.'

enviar_email(destinatario, assunto, corpo)

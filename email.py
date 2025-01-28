import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# função para enviar o e-mail
def enviar_email(remetente, senha, destinatario, assunto, mensagem):
    try:
        # configuração do servidor SMTP
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()  # Inicia a comunicação segura
        servidor.login(remetente, senha)  # Faz o login no servidor de e-mail

        # criação do e-mail
        email = MIMEMultipart()
        email['From'] = remetente
        email['To'] = destinatario
        email['Subject'] = assunto
        email.attach(MIMEText(mensagem, 'plain'))  # Mensagem simples

        # envio do e-mail
        servidor.sendmail(remetente, destinatario, email.as_string())
        servidor.quit()
        print(f"E-mail enviado para {destinatario} com sucesso!")

    except Exception as e:
        print(f"Erro ao enviar e-mail para {destinatario}: {e}")

# dados do remetente
remetente = "seuemail@gmail.com"  # Coloque seu e-mail
senha = "sua_senha"  # Coloque sua senha (use uma senha de app se for Gmail)

# lista de destinatários
contatos = [
    {"nome": "clara", "email": "clara@email.com"},
    {"nome": "ana", "email": "ana@email.com"}
]

# assunto e mensagem
assunto = "Bom dia!"
mensagem_base = "Olá {nome},\n\nEsse é um e-mail automatizado para você!\n\nAtenciosamente,\nEquipe."

# Enviar e-mails personalizados
for contato in contatos:
    mensagem = mensagem_base.format(nome=contato['nome'])  # Personaliza a mensagem
    enviar_email(remetente, senha, contato['email'], assunto, mensagem)

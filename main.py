import os
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.utils import parseaddr

def email_valido(email):
    """Valida se o email está formatado corretamente."""
    return '@' in parseaddr(email)[1]

def main():
    try:
        # Carregar dados dos clientes
        clientes = pd.read_excel('./clientes.xlsx')

        # Conexão com o servidor
        server = smtplib.SMTP('smtp.gmail.com', port=587)
        server.starttls()
        server.login('email_usuario', 'senha_usuario')

        for index, cliente in clientes.iterrows():
            if not email_valido(cliente['email']):
                print(f"Email inválido: {cliente['email']}")
                continue

            # Configuração da mensagem
            msg = MIMEMultipart()
            msg['subject'] = 'Email do Lucas Ineth'
            msg['from'] = 'email_usuario'
            msg['to'] = cliente['email']
            message = f"Olá {cliente['nome']}, você recebeu um email teste :)"
            msg.attach(MIMEText(message, 'plain'))

            # Enviar email
            server.sendmail(msg['from'], msg['to'], msg.as_string())
            print(f"E-mail enviado para {cliente['email']} com sucesso.")

        # Encerrar a conexão com o servidor
        server.quit()

    except Exception as exc:
        print(f"Erro: {exc}")

if __name__ == '__main__':
    main()

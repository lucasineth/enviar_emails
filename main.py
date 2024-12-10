import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

clientes = pd.read_excel('./clientes.xlsx')

for index, cliente in clientes.iterrows():
    msg = MIMEMultipart()
    msg['subject'] = 'Email do Lucas Ramos :)'
    msg['from'] = 'lucasramos1418@gmail.com'
    msg['to'] = cliente['email']
    message = f"Olá {cliente['nome']}, você recebeu um email teste do lucasdev"
    msg.attach(MIMEText(message, 'plain'))
    
    
    
    
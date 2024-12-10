import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

clientes = pd.read_excel('./clientes.xlsx')

for index, cliente in clientes.iterrows():
    print(cliente['nome'], cliente['email'])
    
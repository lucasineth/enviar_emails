# Envio de Emails Automático com Python 📧

Este projeto utiliza Python para enviar emails automaticamente a partir de uma lista de clientes armazenada em um arquivo Excel.

## 📝 Descrição

Este script automatiza o envio de emails personalizados para uma lista de clientes. Ideal para campanhas de marketing, notificações ou mensagens automatizadas.

---

## 📝 Funcionalidades

- Envio de emails em massa com mensagens personalizadas.
- Validação de emails antes do envio.
- Suporte a arquivos Excel para gerenciar a lista de contatos.

---

## 🚀 Tecnologias Utilizadas

- Python 3.8+
- Bibliotecas:
  - `pandas` para manipulação de dados.
  - `smtplib` para envio de emails.
  - `email` para criação de mensagens.
  - `openpyxl` para leitura de arquivos Excel.

## 📦 Requisitos

- Instale as dependências com:
```bash
  pip install pandas openpyxl 
```
## ▶️ Como Usar
* Certifique-se de que o arquivo clientes.xlsx está na raiz do projeto.
* Execute o script:
```bash
    python main.py

```
- O programa enviará os emails e exibirá logs no terminal.


## Configure um arquivo clientes.xlsx com as seguintes colunas:
  - nome: Nome do cliente.
  - email: Endereço de email do cliente.

## ⚠️ Observações
- Certifique-se de que o email configurado permite acesso por aplicativos menos seguros ou utilize uma senha de aplicativo.
- Emails inválidos serão ignorados e notificados no log.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues para sugestões ou relatórios de bugs, e envie um pull request para melhorias.

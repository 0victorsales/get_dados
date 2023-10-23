import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import openpyxl

#SECTION - Funções
def find_emails(s):
    # Expressão regular para detectar endereços de e-mail
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    return re.findall(email_pattern, s)

def find_phone_numbers(s):
    # Expressão regular para detectar os formatos (999) 99999 9999 e (99) 99999-9999
    phone_pattern = r'\(\d{2,3}\)\s?\d{4,5}[-\s]?\d{4}'
    
    return re.findall(phone_pattern, s)


#SECTION - main code

lista_dados = []
file_path  = r"Planilha sem título.xlsx" 
df = pd.read_excel(file_path)

num_linhas = df.shape[0] 

for cont in range(num_linhas):

    cnpj = df.iloc[cont,0]
    razao_social = df.iloc[cont,1]
    
    resposta = requests.get(f'http://cnpj.info/{cnpj}')

    resposta = resposta.text


    # Carregando o conteúdo HTML
    html_content = resposta

    soup = BeautifulSoup(html_content, 'html.parser')

    # Extrair informações principais
    info_dict = {}
    table = soup.find("table")
    for row in table.find_all("tr"):
        key = row.find_all("td")[0].text.strip()
        value = row.find_all("td")[1].text.strip()
        info_dict[key] = value

    # Extrair endereço
    address = " ".join([line.strip() for line in soup.find("h3", text="Endereço").find_next_siblings(text=True, limit=5)])

    # Extrair contatos
    contacts = {}
    for line in soup.find("h3", text="Contatos").find_next_siblings("li"):
        key, value = line.text.split(":", 1)
        contacts[key.strip()] = value.strip()

    # Extrair sócios
    partners = []
    partners_table = soup.find("h3", text="Sócios").find_next_sibling("table")
    for row in partners_table.find_all("tr")[1:]:
        partner = {}
        partner['Código'] = row.find_all("td")[0].text.strip()
        partner['Nome'] = row.find_all("td")[1].text.strip()
        partner['Data de entrada'] = row.find_all("td")[2].text.strip()
        partner['Qualificação'] = row.find_all("td")[3].text.strip()
        partners.append(partner)

    # Extrair atividades de negócios
    activities = []
    activity_headers = soup.find_all("h2")
    for header in activity_headers:
        activity = {}
        activity['Nome'] = header.text.strip()
        activity['Descrição'] = header.find_next_sibling(text=True).strip()
        activities.append(activity)

    # Consolidar os dados extraídos
    extracted_data = {
        "Informação principal": info_dict,
        "Endereço": address,
        "Contatos": contacts,
        "Sócios": partners,
        "Atividades de negócios": activities
    }

    dados_empresa = {}
    # print(extracted_data['Contatos'])
    dados = extracted_data['Contatos']
    string = dados['Telefone(s)']

    dados_email = find_emails(string)
    dados_numero = find_phone_numbers(string)

    dados_empresa["Razão social"] = razao_social
    dados_empresa["cnpj"] = cnpj
    dados_empresa["emails"] = [dados_email[0]] if dados_email else []
    dados_empresa["telefones"] = [dados_numero[0]] if dados_numero else []
    lista_dados.append(dados_empresa)

df = pd.DataFrame(lista_dados)
df.to_excel('lista_dados.xlsx', index=False)

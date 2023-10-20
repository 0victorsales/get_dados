import re

def find_phone_numbers(s):
    # Expressão regular para detectar os formatos (999) 99999 9999 e (99) 99999-9999
    phone_pattern = r'\(\d{2,3}\)\s?\d{4,5}[-\s]?\d{4}'
    
    return re.findall(phone_pattern, s)

# Testando a função
string_input = """ (71) 3034-1040\nFax/mensageiro online: (77) 3423-2787\nCorreio eletrônico: giovanna.jardim@omie.com.vc\nSócios\n\nCódigoNomeData de entradaQualificação\nCPF***158858**Marcelo Paes Jardim2016-05-05Sócio-Administrador\nCPF***150125**Glicio Ricardo Pires Oliveira Junior2020-11-16Sócio\nCPF***989665**Giovanna Prado Paes Jardim2020-11-16Sócio\n\nAtividades de negócios da empresa\n62.09-1-00 - Suporte técnico, manutenção e outros serviços em tecnologia da informação\r\nSuporte técnico, manutenção e outros serviços em tecnologia da informação passaram a desempenhar um papel importantíssimo na vida das empresas com o advento da tecnologia. As demandas são diversas: instalação de softwares e demais aplicativos de informática; manutenção de sistemas de informação; suporte técnico geral às contratantes; e configurações de máquinas e programas. Há ainda os serviços de apoio aos clientes (conhecido como Help-desk); as medidas preventivas e corretivas de segurança da informação (antivírus, firewalls, criptografia, proteção contra hackers, malwares e spywares, dentre outras); e os serviços de recuperação de dados e panes de computadores.\r\ncorreção / remoção de dados"""

phone_numbers = find_phone_numbers(string_input)

print("Números de telefone encontrados:")
for phone in phone_numbers:
    print(phone)





















# import re

# def find_phone_numbers(s):
#     # Expressão regular para detectar números de telefone comuns
#     # Exemplos de formatos suportados: (123) 456-7890, 123-456-7890, 123.456.7890, +31636363634, 075-63546725
#     phone_pattern = r'(\+\d{1,2}\s?)?((\(\d{1,4}\))|\d{1,4})[\s.-]?\d{1,4}[\s.-]?\d{1,4,}'
    
#     return re.findall(phone_pattern, s)

# # Testando a função
# string_input = """ (71) 3034-1040\nFax/mensageiro online: (77) 3423-2787\nCorreio eletrônico: giovanna.jardim@omie.com.vc\nSócios\n\nCódigoNomeData de entradaQualificação\nCPF***158858**Marcelo Paes Jardim2016-05-05Sócio-Administrador\nCPF***150125**Glicio Ricardo Pires Oliveira Junior2020-11-16Sócio\nCPF***989665**Giovanna Prado Paes Jardim2020-11-16Sócio\n\nAtividades de negócios da empresa\n62.09-1-00 - Suporte técnico, manutenção e outros serviços em tecnologia da informação\r\nSuporte técnico, manutenção e outros serviços em tecnologia da informação passaram a desempenhar um papel importantíssimo na vida das empresas com o advento da tecnologia. As demandas são diversas: instalação de softwares e demais aplicativos de informática; manutenção de sistemas de informação; suporte técnico geral às contratantes; e configurações de máquinas e programas. Há ainda os serviços de apoio aos clientes (conhecido como Help-desk); as medidas preventivas e corretivas de segurança da informação (antivírus, firewalls, criptografia, proteção contra hackers, malwares e spywares, dentre outras); e os serviços de recuperação de dados e panes de computadores.\r\ncorreção / remoção de dados"""

# phone_numbers = find_phone_numbers(string_input)

# # A função re.findall retornará tuplas devido aos grupos na regex.
# # Para obter apenas os números de telefone, precisamos pegar o elemento 0 de cada tupla.
# phone_numbers_cleaned = [match[0] for match in phone_numbers]

# print("Números de telefone encontrados:")
# for phone in phone_numbers_cleaned:
#     print(phone)










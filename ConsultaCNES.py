import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#cpfCnes = input(' CNES: ')  11000019640
# 898000204589551 - profissional com dois CNES
# 701203052777417 - profissional com cinco CNES
navegador = webdriver.Chrome()
navegador.get('https://cnes.datasus.gov.br/pages/profissionais/consulta.jsp')
navegador.find_element(By.XPATH, '//*[@id="pesquisaValue"]').send_keys('701203052777417') #Aqui entra o CNES do profssional
navegador.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div/form[3]/div/button').click()
time.sleep(1)
navegador.find_element(By.XPATH, '/html/body/div[2]/main/div/div[2]/div/div[4]/table/tbody/tr/td[3]/button[1]').click()
time.sleep(1)
x = True
ibge = []
cnes = []
#Percorre toda a tabela de estabelecimentos ativos do profissional
for i in range(1,15):
    try:
        ibge.append(navegador.find_element(By.XPATH, f'//*[@id="relatorioGeralField"]/tbody[2]/tr[{i}]/td[1]').text)     #Busca IBGE na tabela
        cnes.append(navegador.find_element(By.XPATH, f'//*[@id="relatorioGeralField"]/tbody[2]/tr[{i}]/td[5]').text)     #Busca CNES na tabela
    except:
        break
#https://cnes2.datasus.gov.br/Mod_Conjunto.asp?VCo_Unidade={IBGE+CNES}
for i in range(0,len(ibge)-1):
    url = f'https://cnes2.datasus.gov.br/Mod_Conjunto.asp?VCo_Unidade={ibge[i]+cnes[i]}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        texto = soup.get_text()
        linhas = texto.split('\n')
        print(f"""
        Nome: {linhas[94]}
        Nome Empresarial: {linhas[104]}
        CEP: {linhas[131]}
        Logradouro: {linhas[117]}, {linhas[118]}
        Complemento: {linhas[129]}
        Bairro: {linhas[130]}
        Municipio: {linhas[132]}
        UF: {linhas[133]}
    """)
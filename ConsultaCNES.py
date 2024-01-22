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
time.sleep(2)
x = True
ibge = []
cnes = []

for i in range(1,15):
    try:
        ibge.append(navegador.find_element(By.XPATH, f'//*[@id="relatorioGeralField"]/tbody[2]/tr[{i}]/td[1]').text)     #Busca IBGE na tabela
        cnes.append(navegador.find_element(By.XPATH, f'//*[@id="relatorioGeralField"]/tbody[2]/tr[{i}]/td[5]').text)     #Busca CNES na tabela
    except:
        print('break1')
        break
    
for i in range(0, len(ibge)-1):
    print(f"""
    IBGE{i+1}: {ibge[i]}
    CNES{i+1}: {cnes[i]}
    """)




"""
PRIMEIRO CAMPO TABELA:
IBGE //*[@id="relatorioGeralField"]/tbody[2]/tr[1]/td[1]
CNES //*[@id="relatorioGeralField"]/tbody[2]/tr[1]/td[5]

SEGUNDO CAMPO TABELA:
IBGE //*[@id="relatorioGeralField"]/tbody[2]/tr[2]/td[1]
CNES //*[@id="relatorioGeralField"]/tbody[2]/tr[2]/td[5]


"""


"""
PRIMEIRO CAMPO TABELA:
IBGE //*[@id="relatorioGeralField"]/tbody[2]/tr[1]/td[1]
CNES //*[@id="relatorioGeralField"]/tbody[2]/tr[1]/td[5]

SEGUNDO CAMPO TABELA:
IBGE //*[@id="relatorioGeralField"]/tbody[2]/tr[2]/td[1]
CNES //*[@id="relatorioGeralField"]/tbody[2]/tr[2]/td[5]

TERCEIRO CAMPO TABELA:
IBGE //*[@id="relatorioGeralField"]/tbody[2]/tr[3]/td[1]
CNES //*[@id="relatorioGeralField"]/tbody[2]/tr[3]/td[5]

QUARTO CAMPO TABELA:
IBGE //*[@id="relatorioGeralField"]/tbody[2]/tr[4]/td[1]
CNES //*[@id="relatorioGeralField"]/tbody[2]/tr[4]/td[5]

QUINTO CAMPO TABELA:
IBGE //*[@id="relatorioGeralField"]/tbody[2]/tr[5]/td[1]
CNES //*[@id="relatorioGeralField"]/tbody[2]/tr[5]/td[5]


"""


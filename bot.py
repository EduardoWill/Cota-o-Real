from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#configuração web driver
service = Service('C:/Users/eduar/Desktop/Cotação/chromedriver.exe')
options = Options()
driver = webdriver.Chrome(service = service, options = options)

driver.get('https://www.bcb.gov.br/')
#Achar os elementos estáticos
real = driver.find_element(By.XPATH, "(//div[@class='d-flex align-items-center justify-content-between'])[1]")
dolar = driver.find_element(By.XPATH, "(//div[@class='d-flex align-items-center justify-content-between'])[2]")
euro = driver.find_element(By.XPATH, "(//div[@class='d-flex align-items-center justify-content-between'])[3]")
seuDinheiro = driver.find_element(By.XPATH, "//input [@aria-label='valorBRL']")
refresh = driver.find_element(By.XPATH, "//button[@aria-label='Converter']")

#Botão
seuDinheiro.send_keys(100 * 100)
refresh.send_keys(Keys.RETURN)
time.sleep(3)
#pegar o valolr dos resultados
dolarValor = driver.find_element(By.XPATH, "//input[@aria-label='valorSaida1']")
valorDol = dolarValor.get_attribute('value')
euroValor = driver.find_element(By.XPATH,("//input[@aria-label='valorSaida2']"))
valorEu = euroValor.get_attribute('value')

print((f'{real.text} Esse valor vale: {dolar.text} {valorDol} {euro.text} {valorEu}'))

input('b')
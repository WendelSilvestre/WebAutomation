from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
import os

load_dotenv()

# abrir um navegador
navegador = webdriver.Chrome("chromedriver.exe")
navegador.get("https://top.gg/bot/432610292342587392/vote")

# Logar 
navegador.find_element(By.XPATH,
    '//*[@id="chakra-modal-13"]/div[2]/a[1]').send_keys(Keys.ENTER)

# Colocar email e senha
navegador.implicitly_wait(10)
navegador.find_element(By.XPATH,
    '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input').send_keys(os.getenv("EMAIL"))
navegador.implicitly_wait(10)
navegador.find_element(By.XPATH,
    '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input').send_keys(os.getenv("PASSWORD"))
navegador.find_element(By.XPATH,
    '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]').send_keys(Keys.ENTER)

# Autorizar 
navegador.find_element(By.XPATH,
    '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/div/div[2]/button[2]').send_keys(Keys.ENTER)

# Votar
navegador.implicitly_wait(100)
navegador.find_element(By.XPATH,
    '//*[@id="__next"]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div[1]/main/div[1]/div/div[2]/button').send_keys(Keys.ENTER)


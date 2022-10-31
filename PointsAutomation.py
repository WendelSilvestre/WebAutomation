from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
import os

load_dotenv()

# abrir um navegador
navegador = webdriver.Chrome("chromedriver.exe")
navegador.get(os.getenv("SITE"))

# Logar
navegador.find_element(By.XPATH,
    '//*[@id="page"]/header/div[4]/div[2]/span[2]').click()
navegador.find_element(By.XPATH,
    '//*[@id="page"]/div[3]/div/div[2]/div/form/div[1]/input').send_keys(os.getenv("EMAIL2"))
navegador.find_element(By.XPATH,
    '//*[@id="page"]/div[3]/div/div[2]/div/form/div[2]/input').send_keys(os.getenv("PASSWORD"))
navegador.find_element(By.XPATH,
    '//*[@id="page"]/div[3]/div/div[2]/div/form/button').send_keys(Keys.ENTER)

navegador.find_element(By.XPATH,
    '//*[@id="page"]/div[1]/div[1]/div[2]/div[2]/section[1]/form/button').send_keys(Keys.ENTER)

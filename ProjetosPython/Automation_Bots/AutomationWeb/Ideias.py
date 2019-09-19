'''
from selenium import webdriver          #WEB
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('http://gangster.goodgamestudios.com/')
driver.find_element(By.CSS_SELECTOR, "#wrapper-game").click()
'''
from pyautogui import click
import pywinauto as py   #DESKTOP
app = py.application.Application(backend="uia").start('C:\Program Files\Anki\Anki.exe')#C:\Program Files\Anki\Anki.exe
dlg_spec = app.LucasAnki
#actionable_dlg = dlg_spec.wait('visible')



'''
arquivopalavras = open("/Users/Lucas/Desktop/Words learned,learning.txt",'r')  #Fez uma lista com as palavras em inglês
leiturapalavras = str(arquivopalavras.read()).split()
print(leiturapalavras)

arquivofrases = open("frases.txt",'r')
def mulipleReplace(text): #tirar caracteres especiais
    for char in ".!?,":
        text = text.replace(char, "")
    return text

leiturafrases = str(arquivofrases.read())
'''





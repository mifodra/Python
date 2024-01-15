## RPA - Automação Bot
# pip install pyautogui
import pyautogui 
import time

# Clicar - pyautogui.click
# Escrever - pyautogui.write("")
# Apertar uma tecla - pyautogui.press("")
# Apertar atalho - pyautogui.hotkey("")

# A cada comando ele faz uma pausa de X segundos
pyautogui.PAUSE = 1

# # # Passo a passo do projeto # # #

# Passo 1 - Entrar no sistema da empresa
    # # https://dlp.hashtagtreinamentos.com/python/intensivao/login
    # apertar a tecla do windows
pyautogui.press("win")
    # digita o nome do programa (chrome)
pyautogui.write("chrome")
    # aperta enter
pyautogui.press("enter")
    # digita o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
    # apertar o enter
pyautogui.press("enter")
    # esperar 5 segundos
time.sleep(5)
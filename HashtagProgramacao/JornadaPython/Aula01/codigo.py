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

# Passo 2 - Fazer login
    # clicar no campo de e-mail
pyautogui.click(x=751, y=470)
    # digitar o email
pyautogui.write("email@gmail.com")
    # passar para o campo de senha
pyautogui.press("tab")
    # digitar a senha
pyautogui.write("minhaSenha")
    # apertar o botão logar
pyautogui.click(x=946, y=676)
time.sleep(3)
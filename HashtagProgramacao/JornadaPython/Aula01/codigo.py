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

# Passo 3 - Importar a base de dados
# pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")

# Passo 4 - Cadastrar um produto
# Passo 5 - Repetir isso até acabar a base de dados
for linha in tabela.index:
        # clicar no campo do produto
    pyautogui.click(x=725, y=323)    
        # escrever o código do produto e descer de campo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
        # escrever a marca e descer de campo
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
        # escrever o tipo e descer de campo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
        # escrever o categoria e descer de campo
    pyautogui.write(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
        # escrever o preço e descer de campo
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
        # escrever o custo e descer de campo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
        # escrever o obs e descer de campo
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
        # apertar o botão enviar
    pyautogui.press("tab")
    pyautogui.press("enter")
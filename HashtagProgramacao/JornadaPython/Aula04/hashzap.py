import flet as ft

# Título Hashzap
def main(pagina):
    titulo = ft.Text("Hashzap")
    pagina.add(titulo)

# Botão de Iniciar o chat
    chat = ft.Column()

    def enviar_mensagem(evento):
        # colocar o nome do usuário + mensagem 
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
        chat.controls.append(ft.Text(texto_campo_mensagem))
        # limpar o campo_mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_chat(evento):
        # feche o popup
        popup.open = False
        # tire o botão "Iniciar chat" da tela
        pagina.remove(botao_iniciar)
        # adicionar o nosso chat
        pagina.add(chat)
        # criar o campo de enviar mensagem e  botao de enviar mensagem
        linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
        pagina.add(linha_mensagem)
        # adicionar que usuario entrou no chat
        texto = f"{nome_usuario.value} entrou no chat"
        chat.controls.append(ft.Text(texto))
        pagina.update()
    # Popup
        # Bem vindo ao Hashzap
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
        # Escreva seu nome
    nome_usuario = ft.TextField(label="Escreva seu nome")
        # Entrar no chat
    botao_entrar = ft.ElevatedButton("Entrar", on_click=entrar_chat)
    

    popup = ft.AlertDialog(
        open=False, #popup incia fechado e só abre quando aperta no botão
        modal=True, #modal é o popup que abre no meio da tela
        title=titulo_popup, #titulo do popup
        content=nome_usuario, #conteudo do popup
        actions=[botao_entrar] #lista de botões dentro do popup
        )

    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
    pagina.add(botao_iniciar)

ft.app(main)
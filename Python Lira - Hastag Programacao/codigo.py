# titulo: hashzap
# botão de iniciar chat
    #clicou no botão:
        #popup / modal
            #Titulo: Bem vindo ao hashzap
            #campo: escreva seu nome no chat
            #botão: entra no chat
# chat
# embaixo do chat
    #campo de digite sua msg
    #botão de enviar

#flet -> framework do python
#pip install flet

import flet as ft

def main(pagina):#criar a função principal
    texto=ft.Text("Hashzap")

    chat=ft.Column()# o chat é uma coluna

    def enviar_mensagem_tunel(mensagem):
         #adicione msg no chat
        texto_entrada=ft.Text(mensagem)
        chat.controls.append(texto_entrada)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        print("Enviar mensagem")
        pagina.pubsub.send_all(f"{nome_usuario.value} diz: {campo_mensagem.value}")       
        #limpar o campo msg
        campo_mensagem.value=""
        pagina.update()

    campo_mensagem= ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar=ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar=ft.Row([campo_mensagem,botao_enviar])#para ficar na mesma linha
    def entrar_chat(evento):
        #fechar popup
        popup.open=False
        #tirar botão iniciar chat
        pagina.remove(botao_iniciar)
        #tirar o título
        pagina.remove(texto)
        #criar chat
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        #criar botão enviar
        pagina.add(linha_enviar)
        pagina.update()

    tiutulo_popup=ft.Text("Bem vindo ao Hashzap")
    nome_usuario=ft.TextField(label="Escreva seu nome no chat")
    botao_entrar=ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    popup=ft.AlertDialog(
        open=False,
        modal=True,
        title=tiutulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]#tem que ser em lista
    )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update() #sempre que editar a pag depois de carregada 

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)#cria um botão onde "iniciar chat" é o texto que aparece no botão.
    
    pagina.add(texto)
    pagina.add(botao_iniciar)    

ft.app(target=main, view=ft.WEB_BROWSER) #criar o app chamando a função principal
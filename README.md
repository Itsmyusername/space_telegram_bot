## Переменные окружения

Настройки берутся из переменных окружения. Чтобы их определить, создайте файл .env рядом с main.py и запишите туда данные в таком формате: ```ПЕРЕМЕННАЯ=значение```.

## Доступные переменные:

    NASA_API_KEY — ключ для доступа к API NASA. Нужен только при скачивании картинок.
    TG_BOT_TOKEN — токен бота, который будет постить картинки.
    TG_CHANNEL_ID — id канала, куда будут отправляться картинки.
    POSTING_INTERVAL — интервал публикации картинок в секундах.

Пример:
```
NASA_API_KEY=IZIcZkOfa2eAAlnlPI5KgDtpX3D55McsrXK3qLIR
TG_BOT_TOKEN=1983812:ACAVSXfx6JgY-wib8rgwJ8Q
TG_CHANNEL_ID=-100537018
POSTING_INTERVAL=86400
```
## Запуск

Скачайте код с GitHub. Установите зависимости:
```python
pip install -r requirements.txt
```
Скачайте картинки:
```python
python fetch_spacex_images.py --image-dir=/path/to/image/dir
```
и/или
```python
python fetch_nasa_images.py --image-dir=/path/to/image/dir
```
Скрипт создаст папку, указанную в параметре --image-dir и скачает туда картинки.
Можно не указывать параметр --image-dir, по-умолчанию будет использоваться папка images.
В случае успешного выполнения скрипт ничего не выводит.
Запустите скрипт:
```
python main.py --image-dir=/path/to/image/dir
```
Можно не указывать параметр --image-dir, по-умолчанию будет использоваться папка images.

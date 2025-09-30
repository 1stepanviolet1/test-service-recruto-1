# test-service-recruto-1
Тестовое задание 1 для Recruto

## Setup
```
pip3 install -r requirements.txt
```

## Start 
Выполнить следующие команды из корня проекта в зависимости от вашей системы.

### Linux
```sh
gunicorn -c gunicorn_http.py app:app
```

### Windows
```powershell
waitress-serve --host=localhost --port=8080 app:app
```

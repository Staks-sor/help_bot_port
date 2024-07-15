@echo off
set REMOTE_USERNAME=staks@
set REMOTE_IP=176.123.165.113
set GITHUB_REPO=URL_репозитория_GitHub

echo Подключение к удаленной машине %REMOTE_IP%...
ssh %REMOTE_USERNAME%@%REMOTE_IP%

echo Обновление данных из репозитория GitHub...
cd путь_к_локальному_репозиторию
git pull
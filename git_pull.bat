@echo off

chcp 65001 > nul

set REMOTE_USERNAME=staks
set REMOTE_IP=176.123.165.113

echo Подключение к удаленной машине %REMOTE_IP% и выполнение команд...
ssh %REMOTE_USERNAME%@%REMOTE_IP% "cd help_bot_port && sudo git pull"

echo Программа будет продолжена через 5 секунд...
timeout /t 5 > nul

echo Сессия закрыта

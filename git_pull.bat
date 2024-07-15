@echo off
set REMOTE_USERNAME=staks
set REMOTE_IP=176.123.165.113
set GITHUB_REPO=gh repo clone Staks-sor/help_bot_port

echo Подключение к удаленной машине %REMOTE_IP%...
ssh %REMOTE_USERNAME%@%REMOTE_IP% "cd ~/help_bot_port && git pull"

echo Сессия закрыта

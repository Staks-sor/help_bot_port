@echo off
chcp 65001 > nul

set REMOTE_USERNAME=staks
set REMOTE_IP=176.123.165.113
set GITHUB_REPO=gh repo clone Staks-sor/help_bot_port

echo Подключение к удаленной машине %REMOTE_IP%...
ssh %REMOTE_USERNAME%@%REMOTE_IP% "if [ -d ~/help_bot_port ]; then echo 'Папка help_bot_port существует'; else echo 'Папка help_bot_port не существует'; fi"
echo Сессия закрыта

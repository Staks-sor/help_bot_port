import subprocess

create_users_teleg_bot_username = 'username'
create_users_teleg_bot_pass = 'pass'
# Установка параметров
username = f'{create_users_teleg_bot_username}'
password = f'{create_users_teleg_bot_pass}'
domain = 'stas-sor.ru'
quota = 50

# Создание SQL-команды
sql_command = f"bash create_mail_user_SQL.sh {username}@{domain} '{password}' > /tmp/user.sql"

# Выполнение SQL-команды
subprocess.run(sql_command, shell=True)

# Выполнение SQL-команды в базе данных
subprocess.run("su - postgres", shell=True)
subprocess.run("psql -d vmail", shell=True)
subprocess.run("\\i /tmp/user.sql", shell=True)

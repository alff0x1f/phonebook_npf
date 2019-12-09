### Задание

Необходимо реализовать веб-приложение &quot;Телефонный справочник&quot; со следующим
функционалом:

- добавление записей;
- просмотр списка существующих записей;
- редактирование записей;
- удаление записей.

Каждая запись должна содержать номер телефона, ФИО и адрес.

### Инструкция о том как развернуть локальную копию:

(В системе должен быть установлен python3 и virtualenv, проверена работа на ubuntu, но на других linux-дистрибутивах тоже должно запуститься без проблем)

```
git clone https://github.com/alff0x1f/phonebook_npf.git
cd phonebook_npf
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd phonebook
./manage.py migrate
./manage.py runserver
```

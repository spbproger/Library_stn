# Приложение - Библиотека для дома

**Для установки на своем ПК требуется выполнить шаги:**
1. Скачать  настоящее приложение по [ссылке](https://github.com/spbproger/Library_stn.git)
2. Открыть приложение в своем IDE
3. Установить Docker по [ссылке](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module)
4. Запустить установку контейнера с приложением командой `docker compose up -d --build`
5. Выполнить в терминале своего IDE следующие моменты:
	- создать суперюзера командой `python manage.py runserver 8000`
	- переименовать файл **.env_example** в **.env_docker** и сменить значения переменных `на собственные`
	- запустить сервер приложения `python manage.py runserver 8000`
7. Перейти в браузере по адресу `127.0.0.1:8000/admin`

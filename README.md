Для запуска бота нужно задать переменную окружения `TELEGRAM_TOKEN` и запустить сервер redis на порту 6379:
```
python3 bot/main.py
```

Сборка Docker-образа:
```
docker build -t <tag> -f Docker/Dockerfile .
```

Запуск контейнера:
```
sudo docker run 
  -e TELEGRAM_TOKEN=$TELEGRAM_TOKEN
  <tag>
```

---

Для работы CD на машине нужно:
- установить Docker
- задать переменную окружения `TELEGRAM_TOKEN`
- загрузить директорию `Docker` и вызвать `docker compose up`

При добавлении тега `v*` или релизе на ветке `main` средствами GitHub Actions собирается Docker-образ с ботом и загружается в [регистр](https://hub.docker.com/repository/docker/trickman/klub_ok_tg_bot/general). Watchtower на настроенном сервере в случае обновления образа в регистре скачивает его и перезапускает локальный контейнер.

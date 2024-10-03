## Описание

Django приложение с реализованным post запросом на сохранение данных по url /api/blender/save_path/.

Выполнено в рамках тестового задания.

## Установка

### Скрипт
Для простоты установки написан простенький скрипт.
```bash
sudo chmod +x install.ssh
. install.ssh
```

### Ручная установка

- Добавляем репозиторий докер
```bash
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
echo "deb [arch=amd64] https://download.docker.com/linux/$(lsb_release -si | tr '[:upper:]' '[:lower:]') $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list
```

- Обновляем и устанавливаем все зависимости
```bash
sudo apt update
sudo apt install -y git docker-ce apt-transport-https ca-certificates curl software-properties-common sqlite3
```

- Клонируем репозиторий
```bash
git clone https://github.com/Omoluzu/astudio_site_info_save_blender_data.git
cd astudio_site_info_save_blender_data
```

- Создаем пустою базу данных
```bash
sqlite3 astudio_site/db.sqlite3 ""
```

- Запускаем сборку докер образа
```bash
sudo systemctl start docker
sudo docker compose up
```

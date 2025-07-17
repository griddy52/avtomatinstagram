# Instagram Reels Automation Service

Веб-сервис для автоматизации публикации контента в Instagram Reels с управлением 50+ аккаунтами. Готов к деплою на Render.com.

## Быстрый старт

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/griddy52/avtomatinstagram.git
   cd avtomatinstagram
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Запустите приложение:
   ```bash
   flask run
   ```

## Деплой на Render.com
- Используйте Dockerfile и render.yaml из репозитория.
- Добавьте переменные окружения из `.env.example`.
- Настройте persistent disk для папки `content/`.

## Структура проекта
- Backend: Flask, SQLAlchemy, APScheduler
- Frontend: HTML5, CSS3, JS (Vanilla)
- Интеграция с Instagram Graph API

## Документация
- Подробное ТЗ и чек-лист — см. в репозитории. 
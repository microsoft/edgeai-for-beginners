# Руководство по интеграции Open WebUI + Foundry Local

Это руководство объясняет, как подключить Open WebUI к Microsoft Foundry Local для создания профессионального интерфейса, похожего на ChatGPT, с использованием ваших локальных AI-моделей.

## Обзор

Open WebUI предоставляет современный, удобный интерфейс для общения, который может подключаться к любому API, совместимому с OpenAI. Подключив его к Foundry Local, вы получите:

- **Профессиональный интерфейс**: Интерфейс, похожий на ChatGPT, с современным дизайном
- **Локальная конфиденциальность**: Вся обработка данных происходит на вашем устройстве
- **Переключение моделей**: Легкое переключение между различными локальными моделями
- **История общения**: Сохранение истории чатов и контекста
- **Загрузка файлов**: Анализ документов и обработка файлов
- **Настраиваемые персонажи**: Системные подсказки и настройка ролей

## Предварительные требования

### Необходимое программное обеспечение

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Загрузка модели

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Быстрая настройка (рекомендуется)

### Шаг 1: Запуск Open WebUI с помощью Docker

```cmd
# Pull the latest Open WebUI image
docker pull ghcr.io/open-webui/open-webui:main

# Run Open WebUI connected to Foundry Local
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  -v open-webui-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

**Windows PowerShell:**
```powershell
docker run -d `
  --name open-webui `
  -p 3000:8080 `
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 `
  -e OPENAI_API_KEY=foundry-local-key `
  -v open-webui-data:/app/backend/data `
  ghcr.io/open-webui/open-webui:main
```

### Шаг 2: Первоначальная настройка

1. **Откройте браузер**: Перейдите на `http://localhost:3000`
2. **Создайте аккаунт**: Настройте учетную запись администратора (первый пользователь становится администратором)
3. **Проверьте подключение**: Модели должны автоматически появиться в выпадающем списке

### Шаг 3: Тестирование подключения

1. Выберите модель из выпадающего списка (например, "phi-4-mini")
2. Введите тестовое сообщение: "Привет! Можешь представиться?"
3. Вы должны увидеть потоковый ответ от вашей локальной модели

## Расширенная настройка

### Переменные окружения

| Переменная | Назначение | Значение по умолчанию | Пример |
|------------|------------|-----------------------|--------|
| `OPENAI_API_BASE_URL` | Endpoint Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API-ключ (требуется, но локально не используется) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Ключ шифрования сессии | автоматически генерируется | `your-secret-key` |
| `ENABLE_SIGNUP` | Разрешить регистрацию новых пользователей | `True` | `False` |

### Ручная настройка (альтернатива)

Если переменные окружения не работают, настройте вручную:

1. **Откройте настройки**: Нажмите на значок шестеренки
2. **Перейдите в раздел "Подключения"**: Настройки → Подключения → OpenAI
3. **Укажите данные API**:
   - Базовый URL API: `http://host.docker.internal:51211/v1`
   - API-ключ: `foundry-local-key` (можно указать любое значение)
4. **Сохраните и протестируйте**: Нажмите "Сохранить", затем протестируйте с моделью

### Постоянное хранение данных

Для сохранения истории общения и настроек:

```cmd
# Windows - Create data directory
mkdir %USERPROFILE%\openwebui-data

# Run with persistent storage
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  -v "%USERPROFILE%\openwebui-data:/app/backend/data" \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## Устранение неполадок

### Проблемы с подключением

**Проблема**: "Connection refused" или модели не загружаются

**Решения**:
```cmd
# 1. Verify Foundry Local is running
foundry service status
foundry service ps

# 2. Test API endpoint directly
curl http://localhost:51211/v1/models

# 3. Check Docker container logs
docker logs open-webui

# 4. Restart Open WebUI container
docker restart open-webui
```

### Модель не отображается

**Проблема**: Open WebUI не показывает модели в выпадающем списке

**Шаги диагностики**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Решение**: Убедитесь, что модель загружена корректно:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Проблемы с сетью Docker

**Проблема**: `host.docker.internal` не разрешается

**Решение для Windows**:
```cmd
# Use localhost alternative (may need admin privileges)
docker run -d \
  --name open-webui \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

**Альтернатива**: Найдите IP-адрес вашего устройства:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Проблемы с производительностью

**Медленные ответы**:
1. Убедитесь, что модель использует ускорение GPU: `foundry service ps`
2. Проверьте наличие достаточных системных ресурсов (ОЗУ/память GPU)
3. Для тестирования используйте более компактную модель

**Проблемы с памятью**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Руководство по использованию

### Основной чат

1. **Выберите модель**: Выберите из выпадающего списка (показывает модели Foundry Local)
2. **Введите сообщение**: Используйте текстовое поле внизу
3. **Отправьте**: Нажмите Enter или кнопку отправки
4. **Просмотрите ответ**: Ответ будет отображаться в режиме реального времени

### Расширенные функции

**Загрузка файлов**:
1. Нажмите на значок скрепки
2. Загрузите документ (PDF, TXT и т.д.)
3. Задавайте вопросы о содержимом
4. Модель проанализирует и ответит на основе документа

**Настраиваемые системные подсказки**:
1. Настройки → Персонализация
2. Установите пользовательскую системную подсказку
3. Создайте постоянный стиль поведения/личность AI

**Управление беседами**:
- **Новый чат**: Нажмите "+" для начала новой беседы
- **История чатов**: Доступ к предыдущим беседам через боковую панель
- **Экспорт**: Скачайте историю чатов в формате текст/JSON

**Сравнение моделей**:
1. Откройте несколько вкладок браузера с Open WebUI
2. Выберите разные модели в каждой вкладке
3. Сравните ответы на одинаковые запросы

### Шаблоны интеграции

**Рабочий процесс разработки**:
```cmd
# Terminal 1: Start Foundry Local with development model
foundry model run phi-4-mini

# Terminal 2: Start Open WebUI for testing
docker run --rm -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=dev-key \
  ghcr.io/open-webui/open-webui:main

# Terminal 3: Test API directly for debugging
curl -X POST http://localhost:51211/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"phi-4-mini","messages":[{"role":"user","content":"test"}]}'
```

## Развертывание в продакшене

### Безопасная настройка

```cmd
# Generate secure secret key
openssl rand -base64 32

# Production deployment with security
docker run -d \
  --name open-webui-prod \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-prod \
  -e WEBUI_SECRET_KEY=your-secure-key-here \
  -e ENABLE_SIGNUP=False \
  -v /path/to/secure/storage:/app/backend/data \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

### Настройка для нескольких пользователей

```cmd
# Allow controlled user registration
docker run -d \
  --name open-webui-team \
  -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-team \
  -e ENABLE_SIGNUP=True \
  -e WEBUI_SECRET_KEY=team-secret-key \
  -v team-data:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### Мониторинг и логирование

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Очистка

```cmd
# Stop Open WebUI
docker stop open-webui

# Remove container
docker rm open-webui

# Remove data volume (WARNING: deletes all chats)
docker volume rm open-webui-data

# Remove image
docker rmi ghcr.io/open-webui/open-webui:main
```

## Следующие шаги

### Идеи для улучшения

1. **Пользовательские модели**: Добавьте свои собственные модели, прошедшие тонкую настройку, в Foundry Local
2. **Интеграция API**: Подключите внешние API через функции Open WebUI
3. **Обработка документов**: Настройте расширенные RAG-пайплайны
4. **Мультимодальность**: Настройте модели для анализа изображений

### Масштабирование

- **Балансировка нагрузки**: Несколько экземпляров Foundry Local за обратным прокси
- **Маршрутизация моделей**: Разные модели для разных задач
- **Управление ресурсами**: Оптимизация памяти GPU для одновременных пользователей
- **Стратегия резервного копирования**: Регулярное резервное копирование данных бесед и конфигураций

## Ссылки

- [Документация Open WebUI](https://docs.openwebui.com/)
- [Репозиторий Open WebUI на GitHub](https://github.com/open-webui/open-webui)
- [Документация Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Руководство по установке Docker](https://docs.docker.com/get-docker/)

---


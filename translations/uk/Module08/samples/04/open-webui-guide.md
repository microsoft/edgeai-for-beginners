# Інструкція з інтеграції Open WebUI + Foundry Local

Ця інструкція показує, як підключити Open WebUI до Microsoft Foundry Local для створення професійного інтерфейсу, схожого на ChatGPT, який працює на ваших локальних AI-моделях.

## Огляд

Open WebUI забезпечує сучасний, зручний інтерфейс чату, який може підключатися до будь-якого API, сумісного з OpenAI. Підключивши його до Foundry Local, ви отримуєте:

- **Професійний інтерфейс**: Інтерфейс, схожий на ChatGPT, із сучасним дизайном
- **Локальна конфіденційність**: Усі обчислення виконуються на вашому пристрої
- **Перемикання моделей**: Легке перемикання між різними локальними моделями
- **Історія розмов**: Збереження історії чату та контексту
- **Завантаження файлів**: Аналіз документів і обробка файлів
- **Кастомні персонажі**: Налаштування системних підказок і ролей

## Попередні вимоги

### Необхідне програмне забезпечення

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Завантаження моделі

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Швидке налаштування (рекомендовано)

### Крок 1: Запуск Open WebUI через Docker

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

### Крок 2: Початкове налаштування

1. **Відкрийте браузер**: Перейдіть за адресою `http://localhost:3000`
2. **Створіть обліковий запис**: Налаштуйте адміністратора (перший користувач стає адміністратором)
3. **Перевірте підключення**: Моделі повинні автоматично з'явитися у випадаючому списку

### Крок 3: Тестування підключення

1. Виберіть вашу модель у випадаючому списку (наприклад, "phi-4-mini")
2. Введіть тестове повідомлення: "Привіт! Можете представитися?"
3. Ви повинні побачити потокову відповідь від вашої локальної моделі

## Розширене налаштування

### Змінні середовища

| Змінна | Призначення | Значення за замовчуванням | Приклад |
|--------|-------------|---------------------------|---------|
| `OPENAI_API_BASE_URL` | Endpoint Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API-ключ (вимагається, але локально не використовується) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Ключ шифрування сесії | автоматично генерується | `your-secret-key` |
| `ENABLE_SIGNUP` | Дозволити реєстрацію нових користувачів | `True` | `False` |

### Ручне налаштування (альтернатива)

Якщо змінні середовища не працюють, налаштуйте вручну:

1. **Відкрийте налаштування**: Натисніть на значок налаштувань (шестерня)
2. **Перейдіть до підключень**: Налаштування → Підключення → OpenAI
3. **Вкажіть дані API**:
   - Базова URL-адреса API: `http://host.docker.internal:51211/v1`
   - API-ключ: `foundry-local-key` (будь-яке значення підійде)
4. **Збережіть і протестуйте**: Натисніть "Зберегти", а потім протестуйте модель

### Збереження даних

Для збереження історії розмов і налаштувань:

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

## Вирішення проблем

### Проблеми з підключенням

**Проблема**: "Connection refused" або моделі не завантажуються

**Рішення**:
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

### Модель не з'являється

**Проблема**: Open WebUI не показує моделі у випадаючому списку

**Кроки для діагностики**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Виправлення**: Переконайтеся, що модель правильно завантажена:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Проблеми з мережею Docker

**Проблема**: `host.docker.internal` не вирішується

**Рішення для Windows**:
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

**Альтернатива**: Знайдіть IP вашого пристрою:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Проблеми з продуктивністю

**Повільні відповіді**:
1. Перевірте, чи модель використовує GPU: `foundry service ps`
2. Переконайтеся, що є достатньо системних ресурсів (RAM/пам'ять GPU)
3. Для тестування використовуйте меншу модель

**Проблеми з пам'яттю**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Інструкція з використання

### Основний чат

1. **Виберіть модель**: Виберіть із випадаючого списку (показує моделі Foundry Local)
2. **Введіть повідомлення**: Використовуйте текстове поле внизу
3. **Надішліть**: Натисніть Enter або кнопку "Надіслати"
4. **Перегляньте відповідь**: Побачте потокову відповідь у реальному часі

### Розширені функції

**Завантаження файлів**:
1. Натисніть на значок скріпки
2. Завантажте документ (PDF, TXT тощо)
3. Задайте питання про зміст
4. Модель проаналізує і відповість на основі документа

**Кастомні системні підказки**:
1. Налаштування → Персоналізація
2. Встановіть кастомну системну підказку
3. Створює стабільну особистість/поведінку AI

**Управління розмовами**:
- **Нова розмова**: Натисніть "+" для початку нової розмови
- **Історія чату**: Доступ до попередніх розмов через бічну панель
- **Експорт**: Завантажте історію чату у форматі текст/JSON

**Порівняння моделей**:
1. Відкрийте кілька вкладок браузера з тим самим Open WebUI
2. Виберіть різні моделі у кожній вкладці
3. Порівняйте відповіді на однакові запити

### Шаблони інтеграції

**Робочий процес розробки**:
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

## Розгортання у продакшн

### Безпечне налаштування

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

### Налаштування для кількох користувачів

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

### Моніторинг і логування

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Очищення

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

## Наступні кроки

### Ідеї для покращення

1. **Кастомні моделі**: Додайте власні моделі, налаштовані під Foundry Local
2. **Інтеграція API**: Підключення до зовнішніх API через функції Open WebUI
3. **Обробка документів**: Налаштуйте розширені RAG-пайплайни
4. **Мультимодальність**: Налаштуйте моделі для аналізу зображень

### Масштабування

- **Балансування навантаження**: Кілька екземплярів Foundry Local за реверс-проксі
- **Маршрутизація моделей**: Різні моделі для різних сценаріїв використання
- **Управління ресурсами**: Оптимізація пам'яті GPU для одночасних користувачів
- **Стратегія резервного копіювання**: Регулярне резервне копіювання даних розмов і конфігурацій

## Посилання

- [Документація Open WebUI](https://docs.openwebui.com/)
- [Репозиторій Open WebUI на GitHub](https://github.com/open-webui/open-webui)
- [Документація Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Інструкція з встановлення Docker](https://docs.docker.com/get-docker/)

---


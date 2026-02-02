# Ръководство за интеграция на Open WebUI + Foundry Local

Това ръководство показва как да свържете Open WebUI с Microsoft Foundry Local за професионален интерфейс, подобен на ChatGPT, захранван от вашите локални AI модели.

## Общ преглед

Open WebUI предоставя модерен, удобен за потребителя чат интерфейс, който може да се свърже с всяко OpenAI-съвместимо API. Чрез свързването му с Foundry Local получавате:

- **Професионален интерфейс**: Интерфейс, подобен на ChatGPT, с модерен дизайн
- **Локална поверителност**: Цялата обработка се извършва на вашето устройство
- **Смяна на модели**: Лесно превключване между различни локални модели
- **История на разговорите**: Постоянна история на чата и контекст
- **Качване на файлове**: Анализ на документи и обработка на файлове
- **Персонализирани роли**: Системни подсказки и персонализация на роли

## Предпоставки

### Необходим софтуер

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Зареждане на модел

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Бърза настройка (Препоръчително)

### Стъпка 1: Стартирайте Open WebUI с Docker

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

### Стъпка 2: Първоначална настройка

1. **Отворете браузър**: Отидете на `http://localhost:3000`
2. **Създайте акаунт**: Настройте администраторски потребител (първият потребител става администратор)
3. **Проверете връзката**: Моделите трябва автоматично да се появят в падащото меню

### Стъпка 3: Тествайте връзката

1. Изберете вашия модел от падащото меню (например "phi-4-mini")
2. Напишете тестово съобщение: "Здравей! Можеш ли да се представиш?"
3. Трябва да видите потоков отговор от вашия локален модел

## Разширена конфигурация

### Променливи на средата

| Променлива | Цел | По подразбиране | Пример |
|------------|-----|-----------------|--------|
| `OPENAI_API_BASE_URL` | Endpoint на Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API ключ (задължителен, но не се използва локално) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Ключ за криптиране на сесията | автоматично генериран | `your-secret-key` |
| `ENABLE_SIGNUP` | Позволяване на регистрация на нови потребители | `True` | `False` |

### Ръчна конфигурация (алтернатива)

Ако променливите на средата не работят, конфигурирайте ръчно:

1. **Отворете Настройки**: Кликнете върху иконата на зъбно колело
2. **Отидете на Връзки**: Настройки → Връзки → OpenAI
3. **Задайте API детайли**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API Key: `foundry-local-key` (всяка стойност работи)
4. **Запазете и тествайте**: Кликнете "Запази", след това тествайте с модел

### Постоянно съхранение на данни

За да запазите разговорите и настройките:

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

## Отстраняване на проблеми

### Проблеми с връзката

**Проблем**: "Connection refused" или моделите не се зареждат

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

### Моделът не се появява

**Проблем**: Open WebUI не показва модели в падащото меню

**Стъпки за отстраняване**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Решение**: Уверете се, че моделът е правилно зареден:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Проблеми с Docker мрежата

**Проблем**: `host.docker.internal` не се разрешава

**Решение за Windows**:
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

**Алтернатива**: Намерете IP адреса на вашата машина:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Проблеми с производителността

**Бавни отговори**:
1. Проверете дали моделът използва GPU ускорение: `foundry service ps`
2. Уверете се, че системните ресурси са достатъчни (RAM/GPU памет)
3. Помислете за използване на по-малък модел за тестване

**Проблеми с паметта**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Ръководство за употреба

### Основен чат

1. **Изберете модел**: Изберете от падащото меню (показва модели на Foundry Local)
2. **Напишете съобщение**: Използвайте текстовото поле в долната част
3. **Изпратете**: Натиснете Enter или кликнете върху бутона за изпращане
4. **Вижте отговора**: Вижте потоковия отговор в реално време

### Разширени функции

**Качване на файлове**:
1. Кликнете върху иконата на кламер
2. Качете документ (PDF, TXT и др.)
3. Задайте въпроси относно съдържанието
4. Моделът ще анализира и отговори въз основа на документа

**Персонализирани системни подсказки**:
1. Настройки → Персонализация
2. Задайте персонализирана системна подсказка
3. Създава последователна личност/поведение на AI

**Управление на разговори**:
- **Нов чат**: Кликнете "+" за започване на нов разговор
- **История на чата**: Достъп до предишни разговори от страничната лента
- **Експорт**: Изтегляне на историята на чата като текст/JSON

**Сравнение на модели**:
1. Отворете няколко раздела в браузъра към същия Open WebUI
2. Изберете различни модели във всеки раздел
3. Сравнете отговорите на едни и същи подсказки

### Модели на интеграция

**Работен процес за разработка**:
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

## Разгръщане в продукция

### Сигурна настройка

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

### Настройка за много потребители

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

### Мониторинг и логове

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Почистване

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

## Следващи стъпки

### Идеи за подобрения

1. **Персонализирани модели**: Добавете свои собствени модели, обучени за Foundry Local
2. **API интеграция**: Свържете се с външни API чрез функции на Open WebUI
3. **Обработка на документи**: Настройте разширени RAG (Retrieval-Augmented Generation) процеси
4. **Мултимодалност**: Конфигурирайте модели за анализ на изображения

### Съображения за мащабиране

- **Баланс на натоварването**: Множество инстанции на Foundry Local зад обратен прокси
- **Рутиране на модели**: Различни модели за различни случаи на употреба
- **Управление на ресурси**: Оптимизация на GPU паметта за едновременни потребители
- **Стратегия за архивиране**: Редовно архивиране на данни от разговори и конфигурации

## Референции

- [Open WebUI Документация](https://docs.openwebui.com/)
- [Open WebUI GitHub Репозитори](https://github.com/open-webui/open-webui)
- [Foundry Local Документация](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Ръководство за инсталиране на Docker](https://docs.docker.com/get-docker/)

---


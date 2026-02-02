# Водич за интеграцију Open WebUI + Foundry Local

Овај водич показује како да повежете Open WebUI са Microsoft Foundry Local ради професионалног интерфејса налик ChatGPT-у, који користи ваше локалне AI моделе.

## Преглед

Open WebUI пружа модеран, кориснички прилагођен интерфејс за ћаскање који се може повезати са било којим API-јем компатибилним са OpenAI. Повезивањем са Foundry Local добијате:

- **Професионални интерфејс**: Интерфејс налик ChatGPT-у са модерним дизајном
- **Локална приватност**: Сва обрада се одвија на вашем уређају
- **Пребацивање модела**: Лако пребацивање између различитих локалних модела
- **Историја разговора**: Перзистентна историја ћаскања и контекст
- **Отпремање датотека**: Анализа докумената и обрада датотека
- **Прилагођене улоге**: Системски промптови и прилагођавање улога

## Предуслови

### Потребан софтвер

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Учитавање модела

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Брза поставка (препоручено)

### Корак 1: Покрените Open WebUI помоћу Docker-а

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

### Корак 2: Почетна поставка

1. **Отворите прегледач**: Идите на `http://localhost:3000`
2. **Креирајте налог**: Поставите администраторског корисника (први корисник постаје администратор)
3. **Потврдите везу**: Модели би требало да се аутоматски појаве у падајућем менију

### Корак 3: Тестирајте везу

1. Изаберите свој модел из падајућег менија (нпр. "phi-4-mini")
2. Унесите тест поруку: "Здраво! Можете ли да се представите?"
3. Требало би да видите стриминг одговор од вашег локалног модела

## Напредна конфигурација

### Енвиронмент променљиве

| Променљива | Сврха | Подразумевано | Пример |
|------------|-------|---------------|--------|
| `OPENAI_API_BASE_URL` | Foundry Local крајња тачка | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API кључ (потребан, али се локално не користи) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Кључ за шифровање сесије | аутоматски генерисан | `your-secret-key` |
| `ENABLE_SIGNUP` | Дозволи регистрацију нових корисника | `True` | `False` |

### Ручна конфигурација (алтернатива)

Ако енвиронмент променљиве не раде, конфигуришите ручно:

1. **Отворите подешавања**: Кликните на Подешавања (икона зупчаника)
2. **Идите на Конекције**: Подешавања → Конекције → OpenAI
3. **Поставите API детаље**:
   - API Base URL: `http://host.docker.internal:51211/v1`
   - API Key: `foundry-local-key` (било која вредност ради)
4. **Сачувајте и тестирајте**: Кликните "Сачувај" па тестирајте са моделом

### Перзистентно складиштење података

Да бисте сачували разговоре и подешавања:

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

## Решавање проблема

### Проблеми са везом

**Проблем**: "Connection refused" или модели се не учитавају

**Решења**:
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

### Модел се не појављује

**Проблем**: Open WebUI не приказује моделе у падајућем менију

**Кораци за отклањање грешке**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Решење**: Уверите се да је модел правилно учитан:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Проблеми са Docker мрежом

**Проблем**: `host.docker.internal` се не разрешава

**Решење за Windows**:
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

**Алтернатива**: Пронађите IP адресе вашег рачунара:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Проблеми са перформансама

**Спори одговори**:
1. Проверите да ли модел користи GPU акцелерацију: `foundry service ps`
2. Уверите се да имате довољно системских ресурса (RAM/GPU меморија)
3. Размотрите коришћење мањег модела за тестирање

**Проблеми са меморијом**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Упутство за коришћење

### Основно ћаскање

1. **Изаберите модел**: Одаберите из падајућег менија (приказује Foundry Local моделе)
2. **Унесите поруку**: Користите текстуални унос на дну
3. **Пошаљите**: Притисните Enter или кликните на дугме за слање
4. **Погледајте одговор**: Видите стриминг одговор у реалном времену

### Напредне функције

**Отпремање датотека**:
1. Кликните на икону спајалице
2. Отпремите документ (PDF, TXT, итд.)
3. Поставите питања о садржају
4. Модел ће анализирати и одговорити на основу документа

**Прилагођени системски промптови**:
1. Подешавања → Персонализација
2. Поставите прилагођени системски промпт
3. Креирајте конзистентну личност/понашање AI-а

**Управљање разговорима**:
- **Ново ћаскање**: Кликните "+" за почетак новог разговора
- **Историја ћаскања**: Приступите претходним разговорима из бочне траке
- **Извоз**: Преузмите историју ћаскања као текст/JSON

**Поређење модела**:
1. Отворите више картица у прегледачу са истим Open WebUI
2. Изаберите различите моделе у свакој картици
3. Упоредите одговоре на исте промптове

### Шаблони интеграције

**Развојни ток**:
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

## Продукционо постављање

### Сигурна поставка

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

### Поставка за више корисника

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

### Праћење и логовање

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Чишћење

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

## Следећи кораци

### Идеје за унапређење

1. **Прилагођени модели**: Додајте своје фино подешене моделе у Foundry Local
2. **API интеграција**: Повежите се са спољним API-јима преко функција Open WebUI
3. **Обрада докумената**: Поставите напредне RAG (Retrieval-Augmented Generation) системе
4. **Мултимодалност**: Конфигуришите моделе за анализу слика

### Разматрања за скалирање

- **Баланс оптерећења**: Више Foundry Local инстанци иза реверсног проксија
- **Рутирање модела**: Различити модели за различите случајеве употребе
- **Управљање ресурсима**: Оптимизација GPU меморије за истовремене кориснике
- **Стратегија резервних копија**: Редовно прављење резервних копија података о разговорима и конфигурацијама

## Референце

- [Open WebUI документација](https://docs.openwebui.com/)
- [Open WebUI GitHub репозиторијум](https://github.com/open-webui/open-webui)
- [Foundry Local документација](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker водич за инсталацију](https://docs.docker.com/get-docker/)

---


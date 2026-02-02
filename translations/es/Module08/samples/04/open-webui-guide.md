# Guía de Integración de Open WebUI + Foundry Local

Esta guía muestra cómo conectar Open WebUI a Microsoft Foundry Local para obtener una interfaz profesional similar a ChatGPT, impulsada por tus modelos de IA locales.

## Resumen

Open WebUI ofrece una interfaz de chat moderna y fácil de usar que puede conectarse a cualquier API compatible con OpenAI. Al conectarlo a Foundry Local, obtienes:

- **Interfaz Profesional**: Una interfaz similar a ChatGPT con diseño moderno
- **Privacidad Local**: Todo el procesamiento ocurre en tu dispositivo
- **Cambio de Modelos**: Cambio sencillo entre diferentes modelos locales
- **Historial de Conversaciones**: Historial de chat persistente y contexto
- **Carga de Archivos**: Capacidades de análisis de documentos y procesamiento de archivos
- **Personas Personalizadas**: Prompts del sistema y personalización de roles

## Requisitos

### Software Necesario

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### Cargar un Modelo

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## Configuración Rápida (Recomendada)

### Paso 1: Ejecutar Open WebUI con Docker

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

### Paso 2: Configuración Inicial

1. **Abrir Navegador**: Navega a `http://localhost:3000`
2. **Crear Cuenta**: Configura un usuario administrador (el primer usuario se convierte en administrador)
3. **Verificar Conexión**: Los modelos deberían aparecer automáticamente en el menú desplegable

### Paso 3: Probar la Conexión

1. Selecciona tu modelo en el menú desplegable (por ejemplo, "phi-4-mini")
2. Escribe un mensaje de prueba: "¡Hola! ¿Puedes presentarte?"
3. Deberías ver una respuesta en tiempo real de tu modelo local

## Configuración Avanzada

### Variables de Entorno

| Variable | Propósito | Predeterminado | Ejemplo |
|----------|-----------|----------------|---------|
| `OPENAI_API_BASE_URL` | Endpoint de Foundry Local | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | Clave API (requerida pero no utilizada localmente) | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | Clave de cifrado de sesión | Generada automáticamente | `your-secret-key` |
| `ENABLE_SIGNUP` | Permitir registro de nuevos usuarios | `True` | `False` |

### Configuración Manual (Alternativa)

Si las variables de entorno no funcionan, configura manualmente:

1. **Abrir Configuración**: Haz clic en Configuración (icono de engranaje)
2. **Ir a Conexiones**: Configuración → Conexiones → OpenAI
3. **Establecer Detalles de API**:
   - URL Base de API: `http://host.docker.internal:51211/v1`
   - Clave API: `foundry-local-key` (cualquier valor funciona)
4. **Guardar y Probar**: Haz clic en "Guardar" y luego prueba con un modelo

### Almacenamiento Persistente de Datos

Para conservar conversaciones y configuraciones:

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

## Resolución de Problemas

### Problemas de Conexión

**Problema**: "Conexión rechazada" o los modelos no se cargan

**Soluciones**:
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

### Modelo No Aparece

**Problema**: Open WebUI no muestra modelos en el menú desplegable

**Pasos de Depuración**:
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**Solución**: Asegúrate de que el modelo esté correctamente cargado:
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Problemas de Red con Docker

**Problema**: `host.docker.internal` no se resuelve

**Solución para Windows**:
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

**Alternativa**: Encuentra la IP de tu máquina:
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### Problemas de Rendimiento

**Respuestas Lentas**:
1. Verifica que el modelo esté utilizando aceleración GPU: `foundry service ps`
2. Asegúrate de tener suficientes recursos del sistema (RAM/memoria GPU)
3. Considera usar un modelo más pequeño para pruebas

**Problemas de Memoria**:
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## Guía de Uso

### Chat Básico

1. **Seleccionar Modelo**: Elige del menú desplegable (muestra modelos de Foundry Local)
2. **Escribir Mensaje**: Usa el campo de texto en la parte inferior
3. **Enviar**: Presiona Enter o haz clic en el botón de enviar
4. **Ver Respuesta**: Observa la respuesta en tiempo real

### Funciones Avanzadas

**Carga de Archivos**:
1. Haz clic en el icono de clip
2. Sube un documento (PDF, TXT, etc.)
3. Haz preguntas sobre el contenido
4. El modelo analizará y responderá basado en el documento

**Prompts Personalizados del Sistema**:
1. Configuración → Personalización
2. Establece un prompt personalizado del sistema
3. Crea una personalidad/comportamiento consistente de la IA

**Gestión de Conversaciones**:
- **Nuevo Chat**: Haz clic en "+" para iniciar una conversación nueva
- **Historial de Chat**: Accede a conversaciones anteriores desde la barra lateral
- **Exportar**: Descarga el historial de chat como texto/JSON

**Comparación de Modelos**:
1. Abre varias pestañas del navegador con el mismo Open WebUI
2. Selecciona diferentes modelos en cada pestaña
3. Compara respuestas a los mismos prompts

### Patrones de Integración

**Flujo de Trabajo de Desarrollo**:
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

## Despliegue en Producción

### Configuración Segura

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

### Configuración Multiusuario

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

### Monitoreo y Registro

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## Limpieza

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

## Próximos Pasos

### Ideas de Mejora

1. **Modelos Personalizados**: Agrega tus propios modelos ajustados a Foundry Local
2. **Integración API**: Conéctate a APIs externas mediante funciones de Open WebUI
3. **Procesamiento de Documentos**: Configura pipelines avanzados de RAG
4. **Multi-Modal**: Configura modelos de visión para análisis de imágenes

### Consideraciones de Escalabilidad

- **Balanceo de Carga**: Múltiples instancias de Foundry Local detrás de un proxy inverso
- **Enrutamiento de Modelos**: Diferentes modelos para diferentes casos de uso
- **Gestión de Recursos**: Optimización de memoria GPU para usuarios concurrentes
- **Estrategia de Respaldo**: Respaldo regular de datos de conversación y configuraciones

## Referencias

- [Documentación de Open WebUI](https://docs.openwebui.com/)
- [Repositorio de GitHub de Open WebUI](https://github.com/open-webui/open-webui)
- [Documentación de Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Guía de Instalación de Docker](https://docs.docker.com/get-docker/)

---


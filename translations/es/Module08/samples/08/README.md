# Windows 11 Chat Sample - Foundry Local

Una aplicación de chat moderna para Windows 11 que integra Microsoft Foundry Local con una hermosa interfaz nativa. Construida con Electron y siguiendo los patrones oficiales de Foundry Local de Microsoft.

## Descripción General

Este ejemplo demuestra cómo crear una aplicación de chat lista para producción que aprovecha modelos de IA locales a través de Foundry Local, ofreciendo a los usuarios conversaciones de IA centradas en la privacidad sin depender de la nube.

## Características

### 🎨 **Diseño Nativo de Windows 11**
- Integración con el sistema Fluent Design
- Efectos de material Mica y transparencia
- Soporte de temas nativos de Windows 11
- Diseño adaptable para todos los tamaños de pantalla
- Cambio automático entre modo oscuro y claro

### 🤖 **Integración de Modelos de IA**
- Integración con el servicio Foundry Local
- Soporte para múltiples modelos con cambio dinámico
- Respuestas en tiempo real por streaming
- Cambio entre modelos locales y en la nube
- Monitoreo de salud y estado de los modelos

### 💬 **Experiencia de Chat**
- Indicadores de escritura en tiempo real
- Persistencia del historial de mensajes
- Exportación de conversaciones de chat
- Prompts personalizados del sistema
- Gestión y ramificación de conversaciones

### ⚡ **Características de Rendimiento**
- Carga diferida y virtualización
- Renderizado optimizado para conversaciones largas
- Precarga de modelos en segundo plano
- Gestión eficiente de memoria
- Animaciones y transiciones fluidas

## Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                    Windows 11 Chat App                     │
├─────────────────┬─────────────────┬─────────────────────────┤
│   Electron UI   │   IPC Bridge    │    Foundry Manager      │
│                 │                 │                         │
│ • Fluent Design │ • Secure Comms  │ • Model Loading         │
│ • Chat Interface│ • Event Routing │ • Health Monitoring     │
│ • Settings      │ • State Sync    │ • Performance Tracking │
│ • Themes        │ • Error Handler │ • Resource Management   │
└─────────────────┴─────────────────┴─────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│               Microsoft Foundry Local Service               │
│                                                             │
│ • Local Model Hosting    • OpenAI API Compatibility        │
│ • Real-time Inference    • Model Catalog Management        │
│ • Streaming Responses    • Health & Status Monitoring      │
└─────────────────────────────────────────────────────────────┘
```

## Requisitos Previos

### Requisitos del Sistema
- **SO**: Windows 11 (22H2 o posterior recomendado)
- **RAM**: Mínimo 8GB, 16GB+ recomendado para modelos más grandes
- **Almacenamiento**: 10GB+ de espacio libre para modelos
- **GPU**: Opcional pero recomendada para inferencias más rápidas

### Dependencias de Software
- **Node.js**: v18.0.0 o posterior
- **Foundry Local**: Última versión de Microsoft
- **Git**: Para clonación y desarrollo

## Instalación

### 1. Instalar Foundry Local
```powershell
# Download from GitHub releases and install
winget install Microsoft.FoundryLocal

# Verify installation
foundry --version
```

### 2. Clonar y Configurar
```bash
# Navigate to sample directory
cd Module08/samples/08

# Install dependencies
npm install

# Install Electron if not global
npm install -g electron
```

### 3. Configurar el Entorno
```powershell
# Optional: Set cloud model credentials for hybrid mode
$env:AZURE_OPENAI_KEY="your-api-key"
$env:AZURE_OPENAI_ENDPOINT="your-endpoint"
$env:AZURE_OPENAI_MODEL="gpt-4"
```

### 4. Ejecutar la Aplicación
```bash
# Development mode
npm start

# Production build
npm run build
npm run dist
```

## Estructura del Proyecto

```
08/
├── README.md                 # This documentation
├── package.json             # Project dependencies and scripts
├── electron.js              # Main Electron process
├── preload.js              # Secure preload script
├── src/
│   ├── index.html          # Main application UI
│   ├── styles/
│   │   ├── fluent.css      # Windows 11 Fluent Design
│   │   ├── chat.css        # Chat interface styles
│   │   └── themes.css      # Light/Dark theme support
│   ├── scripts/
│   │   ├── app.js          # Main application logic
│   │   ├── chat.js         # Chat functionality
│   │   ├── models.js       # Model management
│   │   ├── settings.js     # Settings and preferences
│   │   └── utils.js        # Utility functions
│   └── assets/
│       ├── icons/          # Application icons
│       ├── sounds/         # Notification sounds
│       └── images/         # UI images and illustrations
├── foundry/
│   ├── manager.js          # Foundry Local integration
│   └── health.js           # Health monitoring
└── build/
    ├── icon.ico            # Windows application icon
    └── installer.nsi       # NSIS installer script
```

## Análisis Detallado de Características

### Integración con Windows 11

**Sistema Fluent Design**
- Materiales de fondo Mica
- Efectos de transparencia con acrílico
- Esquinas redondeadas y espaciado moderno
- Paleta de colores nativa de Windows 11
- Tokens de color semántico para accesibilidad

**Características Nativas de Windows**
- Integración de listas de salto para chats recientes
- Notificaciones de Windows para nuevos mensajes
- Progreso en la barra de tareas para operaciones de modelos
- Integración con la bandeja del sistema y acciones rápidas
- Soporte para autenticación con Windows Hello

### Gestión de Modelos de IA

**Modelos Locales**
```javascript
// Automatic model discovery and loading
const models = await foundryManager.discoverModels();
await foundryManager.loadModel('phi-4-mini');

// Model health monitoring
const health = await foundryManager.checkHealth();
console.log(`Model Status: ${health.status}`);
console.log(`Memory Usage: ${health.memoryUsage}MB`);
```

**Soporte Híbrido Nube/Local**
```javascript
// Seamless switching between local and cloud models
if (useCloudModel) {
    await chatManager.switchToCloud('gpt-4');
} else {
    await chatManager.switchToLocal('phi-4-mini');
}
```

### Características de la Interfaz de Chat

**Streaming en Tiempo Real**
- Visualización de respuestas token por token
- Animaciones fluidas de escritura
- Solicitudes cancelables
- Indicadores de escritura y estado

**Gestión de Conversaciones**
- Historial de chat persistente
- Exportación/importación de conversaciones
- Búsqueda y filtrado de mensajes
- Ramificación de conversaciones
- Prompts personalizados del sistema por conversación

**Accesibilidad**
- Navegación completa con teclado
- Compatibilidad con lectores de pantalla
- Soporte para modo de alto contraste
- Tamaños de fuente personalizables
- Integración de entrada por voz

## Ejemplos de Uso

### Integración Básica de Chat
```javascript
// Initialize the chat system
const chat = new ChatManager({
    foundryEndpoint: 'http://localhost:5273',
    defaultModel: 'phi-4-mini',
    streaming: true
});

// Send a message
const response = await chat.sendMessage({
    content: 'Explain quantum computing',
    model: 'phi-4-mini',
    systemPrompt: 'You are a helpful physics teacher.'
});

// Handle streaming responses
chat.on('chunk', (chunk) => {
    appendMessageChunk(chunk.content);
});
```

### Gestión de Modelos
```javascript
// Load a new model
await modelManager.loadModel('qwen2.5-coder-0.5b', {
    showProgress: true,
    autoStart: true
});

// Monitor model performance
modelManager.on('performance', (metrics) => {
    updatePerformanceUI(metrics);
});

// Switch models mid-conversation
await chat.switchModel('phi-4-mini', {
    preserveContext: true
});
```

### Configuración y Personalización
```javascript
// Configure chat behavior
const settings = {
    theme: 'system', // auto, light, dark
    model: 'phi-4-mini',
    streaming: true,
    maxTokens: 1000,
    temperature: 0.7,
    systemPrompt: 'You are a helpful assistant.'
};

await settingsManager.updateSettings(settings);
```

## Opciones de Configuración

### Configuración de la Aplicación
- **Tema**: Automático, modo claro, modo oscuro
- **Modelo**: Selección de modelo predeterminado
- **Rendimiento**: Configuración de inferencia
- **Privacidad**: Políticas de retención de datos
- **Notificaciones**: Alertas de mensajes
- **Atajos**: Atajos de teclado

### Configuración de Chat
- **Streaming**: Activar/desactivar respuestas en tiempo real
- **Longitud de Contexto**: Memoria de conversación
- **Temperatura**: Creatividad de las respuestas
- **Tokens Máximos**: Límites de longitud de respuesta
- **Prompts del Sistema**: Comportamiento predeterminado del asistente

### Configuración de Modelos
- **Descarga Automática**: Actualizaciones automáticas de modelos
- **Tamaño de Caché**: Límites de almacenamiento de modelos locales
- **Modo de Rendimiento**: Preferencias de CPU vs GPU
- **Verificaciones de Salud**: Intervalos de monitoreo

## Desarrollo

### Construcción desde el Código Fuente
```bash
# Install development dependencies
npm install

# Run in development mode
npm run dev

# Build for production
npm run build

# Create installer
npm run dist
```

### Depuración
```bash
# Enable debug mode
set DEBUG=foundry-chat:*
npm start

# View developer tools
# Press F12 in the application
```

### Pruebas
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Run end-to-end tests
npm run test:e2e
```

## Optimización de Rendimiento

### Gestión de Memoria
- Virtualización eficiente de mensajes
- Recolección automática de basura
- Monitoreo de memoria de modelos
- Limpieza de recursos al salir

### Optimización de Renderizado
- Desplazamiento virtual para conversaciones largas
- Carga diferida del historial de mensajes
- Actualizaciones optimizadas de React/DOM
- Animaciones aceleradas por GPU

### Optimización de Red
- Agrupación de conexiones
- Loteo de solicitudes
- Lógica de reintento automático
- Soporte para modo sin conexión

## Consideraciones de Seguridad

### Privacidad de Datos
- Arquitectura centrada en lo local
- Sin transmisión de datos a la nube (modo local)
- Almacenamiento cifrado de conversaciones
- Gestión segura de credenciales

### Seguridad de la Aplicación
- Procesos de renderizado en sandbox
- Política de Seguridad de Contenido (CSP)
- Sin ejecución de código remoto
- Comunicación IPC segura

## Solución de Problemas

### Problemas Comunes

**Foundry Local No Inicia**
```powershell
# Check service status
foundry status

# Restart service
foundry restart

# Check logs
foundry logs
```

**Fallos en la Carga de Modelos**
- Verificar espacio suficiente en disco
- Comprobar conexión a internet para descargas
- Asegurarse de que los controladores de GPU estén actualizados
- Probar variantes diferentes de modelos

**Problemas de Rendimiento**
- Monitorear recursos del sistema
- Ajustar configuración de modelos
- Activar aceleración por hardware
- Cerrar otras aplicaciones que consuman muchos recursos

### Modo de Depuración
Habilitar el registro de depuración configurando variables de entorno:
```powershell
$env:DEBUG="foundry:*"
$env:FOUNDRY_LOG_LEVEL="debug"
```

## Contribuciones

### Configuración para Desarrollo
1. Haz un fork del repositorio
2. Crea una rama para la funcionalidad
3. Instala las dependencias: `npm install`
4. Realiza cambios y prueba
5. Envía una solicitud de extracción

### Estilo de Código
- Configuración de ESLint proporcionada
- Prettier para formato de código
- TypeScript para seguridad de tipos
- Comentarios JSDoc para documentación

## Resultados de Aprendizaje

Después de completar este ejemplo, comprenderás:

1. **Desarrollo Nativo en Windows 11**
   - Implementación del sistema Fluent Design
   - Integración nativa con Windows
   - Mejores prácticas de seguridad en Electron

2. **Integración de Modelos de IA**
   - Arquitectura del servicio Foundry Local
   - Gestión del ciclo de vida de modelos
   - Monitoreo y optimización de rendimiento

3. **Sistemas de Chat en Tiempo Real**
   - Manejo de respuestas por streaming
   - Gestión del estado de conversaciones
   - Patrones de experiencia de usuario

4. **Desarrollo de Aplicaciones para Producción**
   - Manejo de errores y recuperación
   - Optimización de rendimiento
   - Consideraciones de seguridad
   - Estrategias de prueba

## Próximos Pasos

- **Ejemplo 09**: Sistema de Orquestación Multi-Agente
- **Ejemplo 10**: Foundry Local como Integración de Herramientas
- **Temas Avanzados**: Ajuste personalizado de modelos
- **Despliegue**: Patrones de despliegue empresarial

## Licencia

Este ejemplo sigue la misma licencia que el proyecto Microsoft Foundry Local.

---


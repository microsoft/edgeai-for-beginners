# Demo de WebGPU + ONNX Runtime

Este demo muestra cómo ejecutar modelos de IA directamente en el navegador utilizando WebGPU para aceleración de hardware y ONNX Runtime Web.

## Qué Demuestra Esto

- **IA en el navegador**: Ejecuta modelos completamente en el navegador
- **Aceleración con WebGPU**: Inferencia acelerada por hardware cuando está disponible
- **Privacidad ante todo**: Ningún dato sale de tu dispositivo
- **Sin instalación**: Funciona en cualquier navegador compatible
- **Fallback sin problemas**: Cambia al CPU si WebGPU no está disponible

## Requisitos

**Compatibilidad del navegador:**
- Chrome/Edge 113+ con WebGPU habilitado
- Verifica el estado de WebGPU: `chrome://gpu`
- Habilita WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Ejecutar el Demo

### Opción 1: Servidor Local (Recomendado)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Opción 2: Servidor en Vivo de VS Code

1. Instala la extensión "Live Server" en VS Code
2. Haz clic derecho en `index.html` → "Open with Live Server"
3. El demo se abrirá automáticamente en el navegador

## Qué Verás

1. **Detección de WebGPU**: Verifica la compatibilidad del navegador
2. **Carga del Modelo**: Descarga e inicializa el clasificador MNIST
3. **Ejecución de Inferencia**: Realiza predicciones con datos de muestra
4. **Métricas de Rendimiento**: Muestra el tiempo de carga y velocidad de inferencia
5. **Visualización de Resultados**: Confianza de predicción y resultados en bruto

## Rendimiento Esperado

| Proveedor de Ejecución | Carga del Modelo | Inferencia | Notas |
|------------------------|------------------|------------|-------|
| **WebGPU**             | ~2-5s           | ~10-50ms   | Acelerado por hardware |
| **CPU (WASM)**         | ~2-5s           | ~50-200ms  | Fallback por software |

## Solución de Problemas

**WebGPU No Disponible:**
- Actualiza a Chrome/Edge 113+
- Habilita WebGPU en `chrome://flags`
- Verifica que los controladores de GPU estén actualizados
- El demo cambiará automáticamente al CPU

**Errores de Carga:**
- Asegúrate de estar sirviendo vía HTTP (no file://)
- Verifica la conexión de red para la descarga del modelo
- Confirma que CORS no esté bloqueando el modelo ONNX

**Problemas de Rendimiento:**
- WebGPU ofrece una mejora significativa en velocidad frente al CPU
- La primera ejecución puede ser más lenta debido a la descarga del modelo
- Las ejecuciones posteriores usan la caché del navegador

## Integración con Foundry Local

Este demo de WebGPU complementa Foundry Local mostrando:

- **Inferencia en el cliente** para máxima privacidad
- **Capacidades offline** cuando no hay internet disponible  
- **Despliegue en el borde** para entornos con recursos limitados
- **Arquitecturas híbridas** que combinan inferencia local y en servidor

Para aplicaciones en producción, considera:
- Usar Foundry Local para inferencia en el servidor
- Usar WebGPU para preprocesamiento/postprocesamiento en el cliente
- Implementar enrutamiento inteligente entre inferencia local/remota

## Detalles Técnicos

**Modelo Utilizado:**
- Clasificador de dígitos MNIST (formato ONNX)
- Entrada: Imágenes en escala de grises de 28x28
- Salida: Distribución de probabilidad de 10 clases
- Tamaño: ~500KB (descarga rápida)

**ONNX Runtime Web:**
- Proveedor de ejecución WebGPU para aceleración con GPU
- Proveedor de ejecución WASM para fallback en CPU
- Optimización automática y optimización de gráficos

**APIs del Navegador:**
- WebGPU para acceso al hardware
- Web Workers para procesamiento en segundo plano (mejora futura)
- WebAssembly para cálculos eficientes

## Próximos Pasos

- Prueba con modelos ONNX personalizados
- Implementa carga de imágenes reales y clasificación
- Añade inferencia en streaming para modelos más grandes
- Integra entrada de cámara/micrófono

---


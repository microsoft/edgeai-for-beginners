# WebGPU + ONNX Runtime Demo

Este demo mostra como executar modelos de IA diretamente no navegador usando WebGPU para aceleração de hardware e ONNX Runtime Web.

## O Que Este Demo Demonstra

- **IA no Navegador**: Execute modelos inteiramente no navegador
- **Aceleração com WebGPU**: Inferência acelerada por hardware quando disponível
- **Privacidade em Primeiro Lugar**: Nenhum dado sai do seu dispositivo
- **Sem Instalação**: Funciona em qualquer navegador compatível
- **Fallback Suave**: Alterna para CPU se WebGPU não estiver disponível

## Requisitos

**Compatibilidade com Navegadores:**
- Chrome/Edge 113+ com WebGPU habilitado
- Verifique o status do WebGPU: `chrome://gpu`
- Habilite o WebGPU: `chrome://flags/#enable-unsafe-webgpu`

## Executando o Demo

### Opção 1: Servidor Local (Recomendado)

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### Opção 2: Live Server no VS Code

1. Instale a extensão "Live Server" no VS Code
2. Clique com o botão direito em `index.html` → "Open with Live Server"
3. O demo será aberto automaticamente no navegador

## O Que Você Verá

1. **Detecção de WebGPU**: Verifica a compatibilidade do navegador
2. **Carregamento do Modelo**: Faz o download e inicializa o classificador MNIST
3. **Execução de Inferência**: Realiza a previsão em dados de exemplo
4. **Métricas de Desempenho**: Exibe o tempo de carregamento e velocidade de inferência
5. **Exibição de Resultados**: Confiança da previsão e saídas brutas

## Desempenho Esperado

| Provedor de Execução | Carregamento do Modelo | Inferência | Observações |
|-----------------------|------------------------|------------|-------------|
| **WebGPU**           | ~2-5s                 | ~10-50ms   | Acelerado por hardware |
| **CPU (WASM)**       | ~2-5s                 | ~50-200ms  | Alternativa via software |

## Solução de Problemas

**WebGPU Não Disponível:**
- Atualize para Chrome/Edge 113+
- Habilite WebGPU em `chrome://flags`
- Verifique se os drivers da GPU estão atualizados
- O demo alternará automaticamente para CPU

**Erros de Carregamento:**
- Certifique-se de que está servindo via HTTP (não file://)
- Verifique a conexão de rede para o download do modelo
- Confirme que o CORS não está bloqueando o modelo ONNX

**Problemas de Desempenho:**
- WebGPU oferece um aumento significativo de velocidade em relação à CPU
- A primeira execução pode ser mais lenta devido ao download do modelo
- Execuções subsequentes utilizam o cache do navegador

## Integração com Foundry Local

Este demo de WebGPU complementa o Foundry Local ao demonstrar:

- **Inferência no lado do cliente** para máxima privacidade
- **Capacidades offline** quando a internet não está disponível  
- **Implantação na borda** para ambientes com recursos limitados
- **Arquiteturas híbridas** combinando inferência local e remota

Para aplicações em produção, considere:
- Usar Foundry Local para inferência no servidor
- Usar WebGPU para pré-processamento/pós-processamento no cliente
- Implementar roteamento inteligente entre inferência local/remota

## Detalhes Técnicos

**Modelo Utilizado:**
- Classificador de dígitos MNIST (formato ONNX)
- Entrada: Imagens em escala de cinza 28x28
- Saída: Distribuição de probabilidade de 10 classes
- Tamanho: ~500KB (download rápido)

**ONNX Runtime Web:**
- Provedor de execução WebGPU para aceleração via GPU
- Provedor de execução WASM para fallback na CPU
- Otimização automática e otimização de gráficos

**APIs do Navegador:**
- WebGPU para acesso ao hardware
- Web Workers para processamento em segundo plano (melhoria futura)
- WebAssembly para computação eficiente

## Próximos Passos

- Experimente com modelos ONNX personalizados
- Implemente upload de imagens reais e classificação
- Adicione inferência em streaming para modelos maiores
- Integre com entrada de câmera/microfone

---


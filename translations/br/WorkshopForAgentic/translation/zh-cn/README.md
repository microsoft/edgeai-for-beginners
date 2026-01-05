<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aa775a734bda4590ecbe3a94a3b62197",
  "translation_date": "2026-01-05T17:37:47+00:00",
  "source_file": "WorkshopForAgentic/translation/zh-cn/README.md",
  "language_code": "br"
}
-->
# 🎙️ Oficina do Estúdio de Podcast de IA

![logo](../../../../../translated_images/logo.8711e39dc8257d7b.br.png)

## Sua Tarefa

Bem-vindo ao **Estúdio de Podcast de IA**! Você está prestes a lançar seu próprio podcast de tecnologia "Bytes do Futuro" — mas com um toque especial: você vai construir uma equipe de produção movida por IA para te ajudar a criá-lo. Nada mais de pesquisas intermináveis, roteiro e edição de áudio. Em vez disso, você será um produtor de podcast com superpoderes de IA através da programação.

## Contexto da História

Imagine: você e seus amigos querem iniciar um podcast sobre as tendências tecnológicas mais legais, mas todos estão ocupados estudando, trabalhando ou vivendo suas vidas. E se você pudesse construir uma equipe de agentes inteligentes de IA para fazer o trabalho pesado? Um agente faz a pesquisa do tema, outro escreve roteiros envolventes, e um terceiro transforma o texto em diálogos naturais e fluídos. Parece ficção científica? Vamos tornar isso realidade.

## O Que Você Vai Aprender

Ao final desta oficina, você saberá como:
- 🤖 Implantar seu próprio modelo de IA local (sem custo de API, sem depender da nuvem!)
- 🔧 Construir agentes profissionais de IA que colaboram efetivamente
- 🎬 Criar um processo completo de produção de podcast, do conceito ao áudio

## Sua Jornada: Três Atos

Como qualquer boa história, temos três atos. Cada ato constrói gradualmente seu estúdio de podcast IA:

| Capítulo | Sua Tarefa | O Que Acontece | Habilidades Desbloqueadas |
|---------|-----------|--------------|----------------|
| **Ato Um** | [Conheça seu Assistente de IA](01.BuildAIAgentWithSLM.md) | Você vai aprender a criar agentes de IA que podem bater papo, pesquisar na web e até resolver problemas. Pense neles como estagiários que nunca dormem. | 🎯 Construa seu primeiro agente<br>🛠️ Dê superpoderes a ele (ferramentas!)<br>🧠 Ensine-o a pensar<br>🌐 Conecte-o à internet |
| **Ato Dois** | [Monte sua Equipe de Produção](02.AIAgentOrchestrationAndWorkflows.md) | Agora fica divertido! Você vai orquestrar múltiplos agentes de IA para colaborar como um verdadeiro time de podcast. Um pesquisa, outro escreve, você aprova — trabalho em equipe para o sucesso. | 🎭 Coordene múltiplos agentes<br>🔄 Crie fluxos de trabalho de aprovação<br>🖥️ Teste na interface DevUI<br>✋ Mantenha o controle humano |
| **Ato Três** | [Dê Vida ao seu Podcast](03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | O grand finale! Transforme seus roteiros de texto em áudio de podcast real com vozes realistas e conversas naturais. Seu podcast "Bytes do Futuro" está pronto para lançar! | 🎤 Magia de texto para fala<br>👥 Vozes de múltiplos palestrantes<br>⏱️ Áudio de formato longo<br>🚀 Totalmente automatizado |

Cada ato desbloqueia novas habilidades. Se você for corajoso, pode pular etapas, mas recomendamos seguir a ordem!

## Requisitos do Ambiente

Esta oficina suporta vários ambientes de hardware:
- **CPU**: adequado para testes e uso em pequena escala
- **GPU**: recomendado para produção, acelera significativamente a inferência
- **NPU**: suporta a próxima geração de processamento neural acelerado

## O Que Você Precisa

### Lista de Software ✅
- **Python 3.10+** (sua linguagem de programação)
- **Ollama** (para rodar modelos de IA localmente)
- **VS Code** (seu editor de código)
- **Extensão Python** (para deixar o VS Code mais inteligente)
- **Git** (para obter o código)

### Verificação de Hardware 💻
- **Posso rodar?**: 8GB de RAM, 10GB de espaço disponível (funciona, mas pode ser lerdo)
- **Configuração ideal**: 16GB+ de RAM, uma boa GPU (funcionamento suave!)
- **Tem um NPU?**: Isso é melhor ainda! Desbloqueie desempenho de próxima geração 🚀

## Montando Seu Estúdio 🎬

### Passo 1: Atualize o Python

Certifique-se de ter Python 3.10 ou superior:

```bash
python --version
# Deve mostrar Python 3.10.x ou superior
```

Sem Python? Pegue em [python.org](https://python.org) — é grátis!

### Passo 2: Obtenha o Ollama (Seu Executor de Modelos IA)

Vá para [ollama.ai](https://ollama.ai) para baixar o Ollama compatível com seu sistema operacional. Pense nele como o motor que roda modelos de IA localmente.

Verifique se está pronto:

```bash
ollama --version
```

### Passo 3: Baixe Seu Cérebro de IA 🧠

Está na hora de obter o modelo Qwen-3-8B (como contratar seu primeiro assistente de IA):

```bash
ollama pull qwen3:8b
```

*Isso pode levar alguns minutos. Hora perfeita para um café! ☕*

### Passo 4: Configure o VS Code

Se ainda não tem, pegue o [Visual Studio Code](https://code.visualstudio.com/). É o melhor editor de código (disputa aceita 😄).

### Passo 5: Extensão Python

No VS Code:
1. Pressione `Ctrl+Shift+X` (no Mac, `Cmd+Shift+X`)
2. Busque por "Python"
3. Instale a extensão oficial da Microsoft para Python

### Passo 6: Tudo Pronto! 🎉

Sério, você está pronto. Vamos criar um pouco de magia IA!

### Passo 7: Instale o Microsoft Agent Framework e pacotes relacionados 📦

Instale todas as dependências necessárias para a oficina:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Isso vai instalar o Microsoft Agent Framework e todos os pacotes necessários. Tome um café — a primeira instalação pode levar alguns minutos! ☕*

## Notas da Oficina

A estrutura detalhada do projeto, passos de configuração e como executar serão apresentados durante a oficina.

## Solução de Problemas (Quando Algo Der Errado) 🔧

### "Ai, o download do modelo está muito lento!"
**Solução**: Use VPN ou configure fontes espelho para o Ollama. Às vezes a internet não colabora.

### "Meu computador está travando! Falta de memória!"
**Solução**: Troque para um modelo menor ou ajuste `num_ctx` para usar menos memória. Pense nisso como colocar seu IA em dieta.

### "Posso usar GPU para acelerar?"
**Solução**: Ollama detecta GPU automaticamente! Apenas certifique-se de que seus drivers estão atualizados. Aceleração grátis! 🏎️

## Recursos Extras (Para os Curiosos) 📚

- [Documentação Ollama](https://github.com/ollama/ollama) — explore modelos de IA locais
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — aprenda mais sobre a construção de equipes de agentes
- [Informações do Modelo Qwen](https://qwenlm.github.io/) — conheça o cérebro do seu assistente IA

## Licença

Licença MIT — construa coisas incríveis, compartilhe e faça o mundo melhor! 🌍

## Quer Contribuir?

Encontrou um bug? Tem ideias? Abra uma Issue ou PR! Adoramos a vibe da comunidade. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
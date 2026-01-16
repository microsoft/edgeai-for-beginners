<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f94e745264597bc5d8df967ead2eff97",
  "translation_date": "2026-01-05T10:34:16+00:00",
  "source_file": "WorkshopForAgentic/README.md",
  "language_code": "br"
}
-->
# 🎙️ Oficina do Estúdio de Podcast com IA

> 🌏 [中文版 (Versão Chinesa)](translation/zh-cn/README.md)

![logo](../../../translated_images/br/logo.8711e39dc8257d7b.png)

## Sua Missão

Bem-vindo ao **The AI Podcast Studio**! Você está prestes a lançar seu próprio podcast de tecnologia chamado "Future Bytes" — mas aqui está o diferencial: você vai construir uma equipe de produção movida a IA para ajudar você a criá-lo. Chega de horas intermináveis de pesquisa, escrita de roteiros e edição de áudio. Em vez disso, você vai programar seu caminho para se tornar um produtor de podcast com superpoderes de IA.

## A História

Imagine isto: Você e seus amigos querem começar um podcast sobre as tendências tecnológicas mais legais, mas todos estão ocupados com escola, trabalho ou simplesmente a vida. E se você pudesse montar uma equipe de agentes de IA para fazer o trabalho pesado? Um agente pesquisa tópicos, outro escreve roteiros envolventes, e um terceiro transforma texto em conversas com som natural. Parece ficção científica? Vamos tornar real.

## O Que Você Vai Aprender

Ao final desta oficina, você saberá como:
- 🤖 Implantar seu próprio modelo de IA local (sem custos de API, sem dependência de nuvem!)
- 🔧 Construir agentes de IA especializados que realmente trabalham juntos
- 🎬 Criar uma linha completa de produção de podcast do conceito até o áudio

## Sua Jornada: Três Atos

![arch](../../../translated_images/br/arch.5965fe504e4a3a93.png)

Como em toda boa história, temos três atos. Cada um constrói seu estúdio de podcast com IA passo a passo:

| Episódio | Sua Jornada | O Que Acontece | Habilidades Desbloqueadas |
|---------|-----------|--------------|----------------|
| **Ato 1** | [Conheça seus Assistentes de IA](md/01.BuildAIAgentWithSLM.md) | Você descobre como criar agentes de IA que podem conversar, navegar na web e até resolver problemas. Pense neles como seus estagiários de pesquisa que nunca dormem. | 🎯 Construa seu primeiro agente<br>🛠️ Dê superpoderes a ele (ferramentas!)<br>🧠 Ensine a pensar<br>🌐 Conecte à internet |
| **Ato 2** | [Monte sua Equipe de Produção](md/02.AIAgentOrchestrationAndWorkflows.md) | Agora a coisa fica interessante! Você orquestrará múltiplos agentes de IA para trabalharem juntos como um time real de podcast. Um pesquisa, outro escreve, você aprova — trabalho em equipe que funciona. | 🎭 Coordene múltiplos agentes<br>🔄 Construa fluxos de aprovação<br>🖥️ Teste com interface DevUI<br>✋ Mantenha os humanos no controle |
| **Ato 3** | [Dê Vida ao Seu Podcast](md/03.Multi-SpeakerPodcastGenerationWithVibeVoice.md) | O grand finale! Transforme seus roteiros em áudio real de podcast com vozes realistas e conversas naturais. Seu podcast "Future Bytes" está pronto para ir ao ar! | 🎤 Magia do texto para fala<br>👥 Vozes para vários locutores<br>⏱️ Áudio longo<br>🚀 Automação completa |

Cada ato desbloqueia novas habilidades. Pule à frente se for corajoso, mas recomendamos seguir a história!

## Requisitos do Ambiente

Esta oficina suporta vários ambientes de hardware:
- **CPU**: Adequado para testes e uso de pequena escala
- **GPU**: Recomendado para ambientes de produção, melhora significativamente a velocidade de inferência
- **NPU**: Suporta aceleração por unidade neural de próxima geração

## O Que Você Vai Precisar

### Checklist de Software ✅
- **Python 3.10+** (Sua linguagem de programação)
- **Ollama** (Executa modelos de IA na sua máquina)
- **VS Code** (Seu editor de código)
- **Extensão Python** (Deixa o VS Code mais inteligente)
- **Git** (Para pegar o código)

### Checklist de Hardware 💻
- **Posso rodar isso?**: 8GB de RAM, 10GB de espaço livre (funciona, mas pode ser lento)
- **Configuração ideal**: 16GB+ de RAM, uma GPU decente (mais fluido!)
- **Tem um NPU?**: Melhor ainda! Performance de próxima geração desbloqueada 🚀

## Configure Seu Estúdio 🎬

### Passo 1: Potencializando com Python

Certifique-se de que tem Python 3.10 ou superior:

```bash
python --version
# Deve mostrar Python 3.10.x ou superior
```

Sem Python? Baixe em [python.org](https://python.org) — é grátis!

### Passo 2: Baixe o Ollama (Seu Executor de Modelos de IA)

Acesse [ollama.ai](https://ollama.ai) e baixe o Ollama para seu sistema operacional. Pense nele como o motor que roda seus modelos de IA localmente.

Verifique se está pronto:

```bash
ollama --version
```

### Passo 3: Baixe Seu Cérebro de IA 🧠

Hora de pegar o modelo Qwen-3-8B (é como contratar seu primeiro assistente de IA):

```bash
ollama pull qwen3:8b
```

*Pode levar alguns minutos. Hora perfeita para um cafezinho! ☕*

### Passo 4: Instale o VS Code

Baixe o [Visual Studio Code](https://code.visualstudio.com/) se ainda não tiver. É o melhor editor de código que existe (duelo aceito 😄).

### Passo 5: Extensão Python

No VS Code:
1. Pressione `Ctrl+Shift+X` (ou `Cmd+Shift+X` no Mac)
2. Procure por "Python"
3. Instale a extensão oficial da Microsoft para Python

### Passo 6: Você Está Pronto! 🎉

Sério, agora é só mandar ver. Vamos criar magia com IA!

### Passo 7: Instale o Microsoft Agent Framework e Pacotes Relacionados 📦

Instale todas as dependências necessárias para a oficina:

```bash
pip install -r ./Installations/requirements.txt -U
```

*Isso vai instalar o Microsoft Agent Framework e todos os pacotes necessários. Pegue um café — a primeira configuração pode levar alguns minutos! ☕*

## Instruções da Oficina

A estrutura detalhada do projeto, passos de configuração e métodos de execução serão explicados passo a passo durante a oficina.

## Solução de Problemas (Quando Algo Der Errado) 🔧

### "Ai, o download do modelo está demorando uma eternidade!"
**Solução**: Use uma VPN ou configure o Ollama com uma fonte espelho. Às vezes, a internet simplesmente não ajuda.

### "Meu computador está travando! Sem memória!"
**Solução**: Troque para um modelo menor ou ajuste a configuração `num_ctx` para usar menos memória. Pense nisso como colocar sua IA em uma dieta.

### "Posso acelerar isso com minha GPU?"
**Solução**: Ollama detecta GPUs automaticamente! Só certifique-se de que os drivers da GPU estão atualizados. Aceleração grátis! 🏎️

## Recursos Extras (Para os Curiosos) 📚

- [Documentação Ollama](https://github.com/ollama/ollama) — Mergulho profundo em modelos de IA locais
- [Microsoft Agent Framework](https://microsoft.github.io/autogen/) — Saiba mais sobre construção de equipes de agentes
- [Informações do Modelo Qwen](https://qwenlm.github.io/) — Conheça o cérebro do seu assistente de IA

## Licença

Licença MIT — Crie coisas legais, compartilhe, faça o mundo melhor! 🌍

## Quer Contribuir?

Encontrou um bug? Tem uma ideia? Abra uma Issue ou PR! Amamos o clima da comunidade. ✨

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, alertamos que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
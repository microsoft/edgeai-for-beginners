# Oturum 5: Foundry Local ile Hızlı AI Destekli Ajanlar Oluşturma

## Özet

Foundry Local’ın düşük gecikmeli, gizlilik koruyucu çalışma zamanı ile çok rollü AI ajanları tasarlayın ve yönetin. Ajan rolleri, hafıza stratejileri, araç çağırma desenleri ve yürütme grafikleri tanımlayacaksınız. Oturum, Chainlit veya LangGraph ile genişletebileceğiniz iskele desenlerini tanıtır. Başlangıç projesi, mevcut ajan mimarisi örneğini hafıza kalıcılığı ve değerlendirme kancaları eklemek için genişletir.

## Öğrenme Hedefleri

- **Rolleri Tanımlayın**: Sistem istemleri ve yetenek sınırları
- **Hafızayı Uygulayın**: Kısa vadeli (konuşma), uzun vadeli (vektör / dosya), geçici not defterleri
- **İş Akışlarını Oluşturun**: Sıralı, dallanma ve paralel ajan adımları
- **Araçları Entegre Edin**: Hafif işlev araç çağırma deseni
- **Değerlendirin**: Temel izleme + rubrik odaklı sonuç puanlama

## Ön Koşullar

- Oturumlar 1–4 tamamlanmış olmalı
- Python ile `foundry-local-sdk`, `openai`, isteğe bağlı `chainlit`
- Yerel modeller çalışıyor (en az `phi-4-mini`)

### Platformlar Arası Ortam Kod Parçası

Windows:
```powershell
py -m venv .venv
 .\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install foundry-local-sdk openai
```

macOS'tan uzak bir Windows ana bilgisayar hizmetine karşı ajan çalıştırıyorsanız:
```bash
export FOUNDRY_LOCAL_ENDPOINT=http://<windows-host>:5273/v1
```


## Demo Akışı (30 dk)

### 1. Ajan Rolleri ve Hafızayı Tanımlayın (7 dk)

`samples/05-agents/agents_core.py` oluşturun:

```python
#!/usr/bin/env python3
"""Minimal multi-agent scaffolding using Foundry Local (OpenAI-compatible)."""
from openai import OpenAI
from dataclasses import dataclass, field
from typing import List, Dict, Any, Callable
import time, json

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

@dataclass
class AgentMessage:
    role: str
    content: str
    meta: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Agent:
    name: str
    system_prompt: str
    tools: Dict[str, Callable] = field(default_factory=dict)
    memory: List[AgentMessage] = field(default_factory=list)

    def remember(self, role: str, content: str, **meta):
        self.memory.append(AgentMessage(role=role, content=content, meta=meta))

    def context(self, window:int=8):
        recent = self.memory[-window:]
        msgs = [ {"role": "system", "content": self.system_prompt}]
        msgs += [ {"role": m.role, "content": m.content} for m in recent ]
        return msgs

    def act(self, user_input: str, model: str = "phi-4-mini", temperature: float=0.4):
        self.remember("user", user_input)
        resp = client.chat.completions.create(
            model=model,
            messages=self.context() + [{"role": "user", "content": user_input}],
            temperature=temperature,
            max_tokens=400
        )
        answer = resp.choices[0].message.content
        self.remember("assistant", answer, model=model)
        return answer

researcher = Agent(
    name="Researcher",
    system_prompt="You gather factual, structured insights concisely."
)
writer = Agent(
    name="Writer",
    system_prompt="You rewrite content for clarity and engagement while preserving facts."
)

def demo():
    q = "Explain why edge inference matters for privacy and latency."
    r = researcher.act(q)
    print("Researcher ->", r[:200], "...\n")
    w = writer.act(f"Rewrite more user-friendly: {r}")
    print("Writer ->", w[:200], "...")

if __name__ == "__main__":
    demo()
```


### 2. CLI İskele Deseni (3 dk)

```powershell
python samples/05-agents/agents_core.py
```


### 3. Araç Çağırma Ekleyin (7 dk)

`samples/05-agents/tools.py` ile genişletin:

```python
from datetime import datetime
import math, json

def tool_time(_:str)->str:
    return f"Current UTC time: {datetime.utcnow().isoformat()}"

def tool_estimate_tokens(text:str)->str:
    approx = len(text.split()) * 1.35
    return f"Estimated tokens ~ {int(approx)}"

TOOLS = {
    "get_time": tool_time,
    "estimate_tokens": tool_estimate_tokens
}
```

`agents_core.py` dosyasını, basit araç sözdizimini destekleyecek şekilde değiştirin: kullanıcı `#tool:get_time` yazar ve ajan, araç çıktısını üretimden önce bağlama genişletir.

### 4. Orkestrasyon İş Akışı (6 dk)

`samples/05-agents/orchestrator.py` oluşturun:

```python
from agents_core import researcher, writer, Agent
from tools import TOOLS
from openai import OpenAI

client = OpenAI(base_url="http://localhost:5273/v1", api_key="not-needed")

def inject_tools(agent: Agent, user_input: str) -> str:
    if user_input.startswith('#tool:'):
        name = user_input.split(':',1)[1].strip()
        if name in TOOLS:
            out = TOOLS[name](../../../Workshop/"")
            agent.remember("tool", out, tool=name)
            return f"Tool[{name}] => {out}"
    return None

def pipeline(question: str):
    tool_note = inject_tools(researcher, '#tool:get_time')
    r = researcher.act(question)
    w = writer.act(f"Improve readability:\n{r}\nAdd a friendly summary line.")
    return {"raw": r, "refined": w, "tool": tool_note}

if __name__ == '__main__':
    result = pipeline("List three concrete benefits of local SLM inference for regulated industries.")
    for k,v in result.items():
        print(f"== {k.upper()} ==\n{v}\n")
```


### 5. Başlangıç Projesi: `05-agent-architecture` Genişletin (7 dk)

Ekleyin:
1. Kalıcı hafıza katmanı (örneğin, konuşmaların JSON satırlarına eklenmesi)
2. Basit değerlendirme rubriği: gerçeklik / açıklık / stil yer tutucuları
3. İsteğe bağlı Chainlit ön yüzü (iki sekme: konuşma ve izler)
4. İsteğe bağlı LangGraph tarzı durum makinesi (bağımlılık eklenirse) için dallanma kararları

## Doğrulama Kontrol Listesi

```powershell
foundry model run phi-4-mini
python samples/05-agents/orchestrator.py
```

Araç enjeksiyon notu ile yapılandırılmış bir boru hattı çıktısı bekleyin.

## Hafıza Stratejileri Genel Bakış

| Katman | Amaç | Örnek |
|-------|------|-------|
| Kısa vadeli | Diyalog sürekliliği | Son N mesaj |
| Epizodik | Oturum hatırlama | Her oturum için JSON |
| Semantik | Uzun vadeli geri çağırma | Özetlerin vektör deposu |
| Not Defteri | Akıl yürütme adımları | Zincirleme düşünce (özel) |

## Değerlendirme Kancaları (Kavramsal)

```python
evaluation = {
  "factuality": None,  # manual or heuristic
  "clarity": None,
  "style": None,
  "latency_sec": generation_time,
  "model": model_used
}
```


## Sorun Giderme

| Sorun | Sebep | Çözüm |
|------|-------|-------|
| Tekrarlayan cevaplar | Bağlam penceresi çok büyük/küçük | Hafıza pencere parametresini ayarlayın |
| Araç çağrılmadı | Yanlış sözdizimi | `#tool:tool_name` formatını kullanın |
| Yavaş orkestrasyon | Birden fazla soğuk model | Önceden çalıştırma ısınma istemlerini kullanın |

## Referanslar

- Foundry Local SDK: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python
- LangGraph (isteğe bağlı konsept): https://github.com/langchain-ai/langgraph
- Chainlit: https://docs.chainlit.io

---

**Oturum Süresi**: 30 dk  
**Zorluk**: İleri Düzey

## Örnek Senaryo ve Atölye Eşleştirmesi

| Atölye Scripti | Senaryo | Amaç | Örnek İstem |
|----------------|---------|------|-------------|
| `samples/session05/agents_orchestrator.py` / `notebooks/session05_agents_orchestrator.ipynb` | Yönetici dostu özetler üreten bilgi araştırma botu | İki ajanlı boru hattı (araştırma → editoryal düzenleme) isteğe bağlı farklı modellerle | Kenar çıkarımın uyumluluk için neden önemli olduğunu açıklayın. |
| (Genişletilmiş) `tools.py` konsepti | Zaman ve token tahmin araçları ekleyin | Hafif araç çağırma desenini gösterin | #tool:get_time |

### Senaryo Anlatımı
Uyumluluk dokümantasyon ekibinin, taslakları bulut hizmetlerine göndermeden yerel bilgiden hızlı iç özetlere ihtiyacı var. Bir araştırmacı ajan kısa ve gerçekçi maddeler toplar; bir editör ajanı ise yöneticiler için netlik sağlayacak şekilde yeniden yazar. Gecikmeyi optimize etmek için farklı model takma adları atanabilir (hızlı SLM) ve stilistik düzenleme için yalnızca gerektiğinde daha büyük model kullanılabilir.

### Örnek Çoklu Model Ortamı
```powershell
cd Workshop/samples
set AGENT_MODEL_PRIMARY=phi-4-mini
set AGENT_MODEL_EDITOR=gpt-oss-20b
python -m session05.agents_orchestrator
```


### İz Yapısı (İsteğe Bağlı)
```json
{
    "step": 1,
    "agent": "Researcher",
    "latency_ms": 412.3,
    "tokens_in": 22,
    "tokens_out": 168,
    "model": "phi-4-mini"
}
```

Her adımı daha sonra rubrik puanlaması için bir JSONL dosyasına kaydedin.

### İsteğe Bağlı Geliştirmeler

| Tema | Geliştirme | Fayda | Uygulama Taslağı |
|------|-----------|-------|------------------|
| Çoklu Model Rolleri | Her ajan için farklı modeller (`AGENT_MODEL_PRIMARY`, `AGENT_MODEL_EDITOR`) | Uzmanlaşma ve hız | Takma ad ortam değişkenlerini seçin, her rol için takma ad ile `chat_once` çağırın |
| Yapılandırılmış İzler | Her eylemin JSON izi (araç, giriş, gecikme, tokenlar) | Hata ayıklama ve değerlendirme | Listeye sözlük ekleyin; sonunda `.jsonl` yazın |
| Hafıza Kalıcılığı | Yeniden yüklenebilir diyalog bağlamı | Oturum sürekliliği | `Agent.memory`'yi `sessions/<ts>.json` olarak dökün |
| Araç Kaydı | Dinamik araç keşfi | Genişletilebilirlik | `TOOLS` sözlüğünü koruyun ve adları/açıklamaları inceleyin |
| Yeniden Deneme ve Geri Çekilme | Sağlam uzun zincirler | Geçici hataları azaltın | `act`i try/except + üstel geri çekilme ile sarın |
| Rubrik Puanlama | Otomatik nitel etiketler | İyileştirmeleri takip edin | İkinci geçiş modeline istem: "Açıklığı 1-5 arasında değerlendir" |
| Vektör Hafıza | Semantik geri çağırma | Zengin uzun vadeli bağlam | Özetleri gömün, sistem mesajına en iyi k'yi geri çağırın |
| Akış Yanıtları | Algılanan yanıt süresini hızlandırır | UX iyileştirme | Akış kullanılabilir olduğunda kullanın ve kısmi tokenları temizleyin |
| Deterministik Testler | Regresyon kontrolü | Kararlı CI | `temperature=0`, sabit istem tohumları ile çalıştırın |
| Paralel Dallanma | Daha hızlı keşif | Verimlilik | Bağımsız ajan adımları için `concurrent.futures` kullanın |

#### İz Kaydı Örneği

```python
trace.append({
    "agent": agent.name,
    "input": prompt,
    "output_tokens": getattr(usage,'completion_tokens',None),
    "latency_ms": round((end-start)*1000,2),
    "tools_used": list(tool_calls)
})
```


#### Basit Değerlendirme İstemi

```python
score_prompt = f"Rate clarity (1-5) ONLY as a number for this answer:\n{answer}"
rating, _ = chat_once(PRIMARY_ALIAS, messages=[{"role":"user","content":score_prompt}], max_tokens=4, temperature=0)
```

(`answer`, `rating`) çiftlerini kalıcı hale getirerek geçmiş kalite grafiği oluşturun.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.
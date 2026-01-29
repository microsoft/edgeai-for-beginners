# မော်ဂျူး 08 နမူနာများ: Foundry Local Development Guide

## အကျဉ်းချုပ်

ဒီလမ်းညွှန်မှာ **Foundry Local SDK** နဲ့ **Shell Command** နည်းလမ်းတွေကို အသုံးပြုပြီး ထုတ်လုပ်မှုအဆင့် AI အက်ပလီကေးရှင်းတွေကို တည်ဆောက်ဖို့အတွက် အကျယ်တဝင် ပြသထားပါတယ်။ နမူနာတစ်ခုချင်းစီက edge AI တိုးတက်မှုရဲ့ အခြေခံ REST ပေါင်းစည်းမှုကနေ အဆင့်မြင့် multi-agent စနစ်တွေထိ အမျိုးမျိုးသောအချက်အလက်တွေကို ပြသထားပါတယ်။

## တိုးတက်မှုနည်းလမ်း: SDK နှင့် Shell Commands

### Foundry Local SDK ကို အသုံးပြုသင့်သောအခါ:

- **Programmatic Control**: Agent lifecycle, အကဲဖြတ်မှု, ဒါမှမဟုတ် deployment workflows တွေကို အပြည့်အဝထိန်းချုပ်ဖို့လိုအပ်သောအခါ
- **Custom Tooling**: Foundry Local အပေါ် automation တည်ဆောက်ခြင်း (CI/CD ပေါင်းစည်းမှု, multi-agent စီမံခန့်ခွဲမှု)
- **Fine-Grained Access**: Agent metadata, versioning, ဒါမှမဟုတ် evaluation runner control အတွက် အသေးစိတ်ထိန်းချုပ်မှုလိုအပ်သောအခါ
- **Python Integration**: Python အလေးပေးသောပတ်ဝန်းကျင်တွင် အလုပ်လုပ်ခြင်း သို့မဟုတ် Foundry logic ကို ကျယ်ပြန့်သောအက်ပလီကေးရှင်းများထဲတွင် ထည့်သွင်းခြင်း
- **Enterprise Workflows**: Microsoft reference architectures နှင့် ကိုက်ညီသော modular workflows နှင့် reproducible evaluation pipelines တွေကို အကောင်အထည်ဖော်ခြင်း

### Shell Commands ကို အသုံးပြုသင့်သောအခါ:

- **Quick Testing**: အလျင်အမြန် local စမ်းသပ်မှု, manual agent launches, ဒါမှမဟုတ် setup အတည်ပြုမှု
- **CLI Simplicity**: Agent များကို စတင်/ရပ်တန့်ခြင်း, log များစစ်ဆေးခြင်း, ဒါမှမဟုတ် အခြေခံအကဲဖြတ်မှုများအတွက် ရိုးရှင်းသော CLI လုပ်ဆောင်မှုလိုအပ်သောအခါ
- **Lightweight Automation**: SDK integration အပြည့်အဝလိုအပ်မှုမရှိသော ရိုးရှင်းသော automation script ရေးသားခြင်း
- **Rapid Iteration**: Debugging နှင့် တိုးတက်မှုဆိုင်ရာ လှည့်လည်မှုများ, အထူးသဖြင့် အကန့်အသတ်ရှိသောပတ်ဝန်းကျင်များ သို့မဟုတ် resource group-level deployments တွင်
- **Setup & Validation**: စတင်ပတ်ဝန်းကျင် configuration နှင့် အလျင်အမြန်အတည်ပြုမှုလုပ်ဆောင်မှုများ

## အကောင်းဆုံးအလေ့အကျင့်များနှင့် အကြံပြုထားသော Workflow

Agent lifecycle management, dependency tracking, နှင့် least-privilege reproducibility principles အပေါ်အခြေခံပြီး:

### အဆင့် 1: Foundation & Setup
1. **Shell Commands** ကို စတင် setup နှင့် အလျင်အမြန်အတည်ပြုမှုအတွက် အသုံးပြုပါ
2. **Environment ကို အတည်ပြုပါ** CLI tools နှင့် အခြေခံ model deployment ကို အသုံးပြု၍
3. **Connectivity ကို စမ်းသပ်ပါ** ရိုးရှင်းသော REST calls နှင့် health checks များဖြင့်

### အဆင့် 2: Development & Integration
1. **SDK သို့ ပြောင်းရွှေ့ပါ** scalable, traceable workflows များအတွက်
2. **Programmatic Control ကို အကောင်အထည်ဖော်ပါ** complex agent interactions များအတွက်
3. **Custom Tools တည်ဆောက်ပါ** community-ready templates နှင့် Azure OpenAI integration အတွက်

### အဆင့် 3: Production & Scale
1. **Hybrid Approach** ကို CLI ကို ops အတွက်နှင့် SDK ကို application logic အတွက် ပေါင်းစပ်အသုံးပြုပါ
2. **Enterprise Integration** monitoring, logging, နှင့် deployment pipelines များနှင့်
3. **Community Contribution** reusable templates နှင့် အကောင်းဆုံးအလေ့အကျင့်များအားဖြင့်

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားယူမှားမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
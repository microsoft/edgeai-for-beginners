from openai import OpenAI

import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("OPENAI_BASE_URL", "http://127.0.0.1:1234/v1")
MODEL_ID = os.getenv("OPENAI_MODEL_ID", "google/gemma-4-26b-a4b")

client = OpenAI(base_url=BASE_URL, api_key=os.getenv("OPENAI_API_KEY", "not-needed"))

SYSTEM_INSTRUCTIONS = """
        You are my English podcast script generation assistant. Please generate a 10-minute English podcast script based on the provided content.
        Note that the podcast script is co-hosted by host Lucy and expert Ken. The script content is produced based on the input content, and the final output format is as follows:

            speaker 1: …… \n
            speaker 2: …… \n
            speaker 1: …… \n
            speaker 2: …… \n
            speaker 1: …… \n
            speaker 2: …… \n
            """

prompt = """

Artificial Intelligence (AI) is a branch of computer science aimed at developing machines or software capable of simulating human intelligent behavior. Its core goal is to enable machines to possess capabilities such as perception, learning, reasoning, decision-making, and creation, in order to perform tasks that require human intelligence. Below are the key characteristics and application areas of artificial intelligence:

---

### **1. Core Capabilities**
- **Learning Ability**: Automatically improving performance by training models with data (e.g., recommendation systems).
- **Reasoning and Logic**: Solving complex problems (e.g., strategy analysis in board games).
- **Perception**: Sensing the environment through vision (image recognition), hearing (speech recognition), etc.
- **Language Understanding**: Natural Language Processing (NLP), supporting machine translation, chatbots, etc.
- **Autonomous Decision-Making**: Making optimal choices in dynamic environments (e.g., autonomous driving).

---

### **2. Type Classification**
- **Narrow AI**: Focused on specific tasks, such as Siri, facial recognition, and medical image analysis.
- **General AI**: Possessing general cognitive abilities comparable to humans (not yet realized).
- **Super AI**: Surpassing human intelligence, still at the theoretical stage.

---

### **3. Technical Foundations**
- **Machine Learning (ML)**: Learning patterns from data through algorithms (e.g., deep learning, reinforcement learning).
- **Deep Learning (DL)**: Using neural networks to simulate brain structures, excelling at processing unstructured data such as images and speech.
- **Natural Language Processing (NLP)**: Enabling machines to understand and generate human language (e.g., chatbots, text summarization).

---

### **4. Application Scenarios**
- **Healthcare**: Disease diagnosis, drug research and development.
- **Finance**: Risk assessment, quantitative trading.
- **Transportation**: Autonomous driving, traffic flow optimization.
- **Education**: Personalized learning recommendations.
- **Entertainment**: Game AI, content generation.

---

### **5. Challenges and Ethics**
- **Data Privacy**: AI relies on large amounts of data, which may lead to privacy breaches.
- **Algorithmic Bias**: Bias in training data may lead to discriminatory decisions.
- **Employment Impact**: Automation may replace some traditional jobs.
- **Security Risks**: Such as the misuse of deepfake technology.

---

### **6. Development History**
- **1956**: The Dartmouth Conference first proposed the concept of "Artificial Intelligence".
- **1980s**: Expert systems rose, but declined due to limitations.
- **After 2000**: Big data and computing power improvements drove the AI boom, with deep learning becoming mainstream.

---

If you need more specific explanations or examples, feel free to ask! 😊

"""

response = client.chat.completions.create(
    model=MODEL_ID,
    messages=[
        {"role": "system", "content": SYSTEM_INSTRUCTIONS},
        {"role": "user", "content": prompt},
    ],
)

print(response.choices[0].message.content)
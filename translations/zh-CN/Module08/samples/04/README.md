# 示例 04：使用 Chainlit 构建生产级聊天应用

一个全面的示例，展示了使用 Microsoft Foundry Local 构建生产级聊天应用的多种方法，包含现代化的网页界面、流式响应以及先进的浏览器技术。

## 包含内容

- **🚀 Chainlit 聊天应用** (`app.py`)：支持流式响应的生产级聊天应用
- **🌐 WebGPU 演示** (`webgpu-demo/`)：基于浏览器的 AI 推理，支持硬件加速
- **🎨 Open WebUI 集成** (`open-webui-guide.md`)：专业的 ChatGPT 风格界面
- **📚 教学笔记本** (`chainlit_app.ipynb`)：交互式学习材料

## 快速开始

### 1. Chainlit 聊天应用

```cmd
# Navigate to Module08 directory
cd Module08

# Start your model
foundry model run phi-4-mini

# Run Chainlit app (using port 8080 to avoid conflicts)
chainlit run samples\04\app.py -w --port 8080
```

访问地址：`http://localhost:8080`

### 2. WebGPU 浏览器演示

```cmd
# Navigate to WebGPU demo
cd Module08\samples\04\webgpu-demo

# Serve the demo
python -m http.server 5173
```

访问地址：`http://localhost:5173`

### 3. Open WebUI 设置

```cmd
# Run Open WebUI with Docker
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

访问地址：`http://localhost:3000`

## 架构模式

### 本地与云端决策矩阵

| 场景 | 推荐 | 原因 |
|------|------|------|
| **隐私敏感数据** | 🏠 本地 (Foundry) | 数据不会离开设备 |
| **复杂推理** | ☁️ 云端 (Azure OpenAI) | 可访问更大的模型 |
| **实时聊天** | 🏠 本地 (Foundry) | 更低延迟，更快响应 |
| **文档分析** | 🔄 混合 | 本地提取，云端分析 |
| **代码生成** | 🏠 本地 (Foundry) | 隐私保护 + 专用模型 |
| **研究任务** | ☁️ 云端 (Azure OpenAI) | 需要广泛的知识库 |

### 技术对比

| 技术 | 使用场景 | 优点 | 缺点 |
|------|----------|------|------|
| **Chainlit** | Python 开发者，快速原型设计 | 设置简单，支持流式响应 | 仅支持 Python |
| **WebGPU** | 最大隐私，离线场景 | 原生浏览器，无需服务器 | 模型大小有限 |
| **Open WebUI** | 生产部署，团队协作 | 专业界面，用户管理 | 需要 Docker |

## 前置条件

- **Foundry Local**：已安装并运行 ([下载](https://aka.ms/foundry-local-installer))
- **Python**：3.10+，支持虚拟环境
- **模型**：至少加载一个模型 (`foundry model run phi-4-mini`)
- **浏览器**：支持 WebGPU 的 Chrome/Edge，用于演示
- **Docker**：用于 Open WebUI（可选）

## 安装与设置

### 1. Python 环境设置

```cmd
# Navigate to Module08 directory
cd Module08

# Create and activate virtual environment
py -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Foundry Local 设置

```cmd
# Verify Foundry Local installation
foundry --version

# Start the service
foundry service start

# Load a model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## 示例应用

### Chainlit 聊天应用

**功能特点：**
- 🚀 **实时流式响应**：生成的 token 即时显示
- 🛡️ **强大的错误处理**：优雅降级与恢复
- 🎨 **现代化界面**：开箱即用的专业聊天界面
- 🔧 **灵活配置**：支持环境变量与自动检测
- 📱 **响应式设计**：适配桌面与移动设备

**快速开始：**
```cmd
# Run with default settings (recommended)
chainlit run samples\04\app.py -w --port 8080

# Use specific model
set MODEL=qwen2.5-7b
chainlit run samples\04\app.py -w --port 8080

# Manual endpoint configuration
set BASE_URL=http://localhost:51211
set API_KEY=your-api-key
chainlit run samples\04\app.py -w --port 8080
```

### WebGPU 浏览器演示

**功能特点：**
- 🌐 **原生浏览器 AI**：无需服务器，完全在浏览器中运行
- ⚡ **WebGPU 加速**：支持硬件加速
- 🔒 **最大隐私保护**：数据绝不会离开设备
- 🎯 **零安装**：兼容的浏览器即可运行
- 🔄 **优雅回退**：WebGPU 不可用时自动切换到 CPU

**运行方式：**
```cmd
cd samples\04\webgpu-demo
python -m http.server 5173
# Open http://localhost:5173
```

### Open WebUI 集成

**功能特点：**
- 🎨 **ChatGPT 风格界面**：专业且熟悉的用户界面
- 👥 **多用户支持**：用户账户与会话历史记录
- 📁 **文件处理**：上传并分析文档
- 🔄 **模型切换**：轻松切换不同模型
- 🐳 **Docker 部署**：生产级容器化设置

**快速设置：**
```cmd
docker run -d --name open-webui -p 3000:8080 \
  -e OPENAI_API_BASE_URL=http://host.docker.internal:51211/v1 \
  -e OPENAI_API_KEY=foundry-local-key \
  ghcr.io/open-webui/open-webui:main
```

## 配置参考

### 环境变量

| 变量 | 描述 | 默认值 | 示例 |
|------|------|--------|------|
| `MODEL` | 使用的模型别名 | `phi-4-mini` | `qwen2.5-7b` |
| `BASE_URL` | Foundry Local 端点 | 自动检测 | `http://localhost:51211` |
| `API_KEY` | API 密钥（本地可选） | `""` | `your-api-key` |

## 故障排除

### 常见问题

**Chainlit 应用：**

1. **服务不可用：**
   ```cmd
   # Check Foundry Local status
   foundry service status
   foundry service ps
   
   # Validate API endpoint (note: port 51211)
   curl http://localhost:51211/v1/models
   ```

2. **端口冲突：**
   ```cmd
   # Check what's using port 8080
   netstat -ano | findstr :8080
   
   # Use different port if needed
   chainlit run samples\04\app.py -w --port 3000
   ```

3. **Python 环境问题：**
   ```cmd
   # Verify correct interpreter in VS Code
   # Ctrl+Shift+P → Python: Select Interpreter
   # Choose: Module08/.venv/Scripts/python.exe
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

**WebGPU 演示：**

1. **WebGPU 不支持：**
   - 更新到 Chrome/Edge 113+
   - 启用 WebGPU：`chrome://flags/#enable-unsafe-webgpu`
   - 检查 GPU 状态：`chrome://gpu`
   - 演示会自动回退到 CPU

2. **模型加载错误：**
   - 确保网络连接以下载模型
   - 检查浏览器控制台中的 CORS 错误
   - 确保通过 HTTP 服务（而非 file://）

**Open WebUI：**

1. **连接被拒绝：**
   ```cmd
   # Check Docker is running
   docker --version
   
   # Check container status
   docker ps | findstr open-webui
   
   # View container logs
   docker logs open-webui
   ```

2. **模型未显示：**
   ```cmd
   # Verify Foundry Local endpoint
   curl http://localhost:51211/v1/models
   
   # Restart Open WebUI
   docker restart open-webui
   ```

### 验证清单

```cmd
# ✅ 1. Foundry Local Setup
foundry --version                    # Should show version
foundry service status               # Should show "running"
foundry model list                   # Should show loaded models
curl http://localhost:51211/v1/models  # Should return JSON

# ✅ 2. Python Environment  
python --version                     # Should be 3.10+
pip list | findstr chainlit         # Should show chainlit package
pip list | findstr openai           # Should show openai package

# ✅ 3. Application Testing
chainlit run samples\04\app.py -w --port 8080  # Should open browser
# Test WebGPU demo at localhost:5173
# Test Open WebUI at localhost:3000
```

## 高级用法

### 性能优化

**Chainlit：**
- 使用流式响应提升用户体验
- 实现连接池以支持高并发
- 缓存模型响应以处理重复查询
- 监控大规模会话历史的内存使用

**WebGPU：**
- 使用 WebGPU 实现最大隐私与速度
- 实现模型量化以减小模型大小
- 使用 Web Workers 进行后台处理
- 在浏览器存储中缓存编译后的模型

**Open WebUI：**
- 使用持久卷保存会话历史
- 为 Docker 容器配置资源限制
- 实现用户数据的备份策略
- 设置反向代理以支持 SSL 终止

### 集成模式

**本地/云端混合：**
```python
# Route based on complexity and privacy requirements
async def intelligent_routing(prompt: str, metadata: dict):
    if metadata.get("contains_pii"):
        return await foundry_local_completion(prompt)  # Privacy-sensitive
    elif len(prompt.split()) > 200:
        return await azure_openai_completion(prompt)   # Complex reasoning
    else:
        return await foundry_local_completion(prompt)  # Default local
```

**多模态管道：**
```python
# Combine different AI capabilities
async def analyze_document(file_path: str):
    # 1. OCR with WebGPU (browser-based)
    text = await webgpu_ocr(file_path)
    
    # 2. Analysis with Foundry Local (private)
    summary = await foundry_local_analyze(text)
    
    # 3. Enhancement with cloud (if needed)
    if summary.confidence < 0.8:
        summary = await azure_openai_enhance(summary)
    
    return summary
```

## 生产部署

### 安全注意事项

- **API 密钥**：使用环境变量，切勿硬编码
- **网络**：生产环境使用 HTTPS，团队访问可考虑 VPN
- **访问控制**：为 Open WebUI 实现身份验证
- **数据隐私**：审查哪些数据留在本地，哪些发送到云端
- **更新**：保持 Foundry Local 和容器的最新版本

### 监控与维护

- **健康检查**：实现端点监控
- **日志记录**：集中管理所有组件的日志
- **指标监控**：跟踪响应时间、错误率、资源使用情况
- **备份**：定期备份会话数据和配置

## 参考与资源

### 文档
- [Chainlit 文档](https://docs.chainlit.io/) - 完整框架指南
- [Foundry Local 文档](https://learn.microsoft.com/azure/ai-foundry/foundry-local/) - 官方 Microsoft 文档
- [ONNX Runtime Web](https://onnxruntime.ai/docs/get-started/with-javascript/web.html) - WebGPU 集成
- [Open WebUI 文档](https://docs.openwebui.com/) - 高级配置指南

### 示例文件
- [`app.py`](../../../../../Module08/samples/04/app.py) - 生产级 Chainlit 应用
- [`chainlit_app.ipynb`](./chainlit_app.ipynb) - 教学笔记本
- [`webgpu-demo/`](../../../../../Module08/samples/04/webgpu-demo) - 基于浏览器的 AI 推理
- [`open-webui-guide.md`](./open-webui-guide.md) - 完整的 Open WebUI 设置指南

### 相关示例
- [第 4 节文档](../../04.CuttingEdgeModels.md) - 完整课程指南
- [Foundry Local 示例](https://github.com/microsoft/foundry-local/tree/main/samples) - 官方示例

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。
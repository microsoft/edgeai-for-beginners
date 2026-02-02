# Open WebUI + Foundry Local 集成指南

本指南介绍如何将 Open WebUI 与 Microsoft Foundry Local 连接，打造一个由本地 AI 模型驱动的专业 ChatGPT 风格界面。

## 概述

Open WebUI 提供了一个现代化、用户友好的聊天界面，可以连接到任何兼容 OpenAI 的 API。通过将其连接到 Foundry Local，您可以获得以下功能：

- **专业界面**：类似 ChatGPT 的现代化设计
- **本地隐私**：所有处理均在您的设备上完成
- **模型切换**：轻松切换不同的本地模型
- **对话历史**：持久的聊天记录和上下文
- **文件上传**：文档分析和文件处理功能
- **自定义角色**：系统提示和角色定制

## 前提条件

### 必需软件

```cmd
# Verify Foundry Local installation
foundry --version

# Verify Docker installation
docker --version

# Start Foundry Local service
foundry service start
```

### 加载模型

```cmd
# List available models
foundry model list

# Load your preferred model
foundry model run phi-4-mini

# Verify model is running
foundry service ps
```

## 快速设置（推荐）

### 步骤 1：使用 Docker 运行 Open WebUI

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

### 步骤 2：初始设置

1. **打开浏览器**：访问 `http://localhost:3000`
2. **创建账户**：设置管理员用户（第一个用户将成为管理员）
3. **验证连接**：模型应自动出现在下拉菜单中

### 步骤 3：测试连接

1. 从下拉菜单中选择您的模型（例如 "phi-4-mini"）
2. 输入测试消息："你好！你能介绍一下自己吗？"
3. 您应该会看到来自本地模型的流式响应

## 高级配置

### 环境变量

| 变量 | 用途 | 默认值 | 示例 |
|------|------|--------|------|
| `OPENAI_API_BASE_URL` | Foundry Local 端点 | - | `http://host.docker.internal:51211/v1` |
| `OPENAI_API_KEY` | API 密钥（本地使用时必填但不实际使用） | - | `foundry-local-key` |
| `WEBUI_SECRET_KEY` | 会话加密密钥 | 自动生成 | `your-secret-key` |
| `ENABLE_SIGNUP` | 允许新用户注册 | `True` | `False` |

### 手动配置（替代方案）

如果环境变量不起作用，可手动配置：

1. **打开设置**：点击设置（齿轮图标）
2. **导航到连接**：设置 → 连接 → OpenAI
3. **设置 API 详情**：
   - API 基础 URL: `http://host.docker.internal:51211/v1`
   - API 密钥: `foundry-local-key`（任意值均可）
4. **保存并测试**：点击“保存”，然后使用模型进行测试

### 持久化数据存储

要持久化对话和设置：

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

## 故障排除

### 连接问题

**问题**："连接被拒绝" 或模型未加载

**解决方案**：
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

### 模型未显示

**问题**：Open WebUI 下拉菜单中没有显示模型

**调试步骤**：
```cmd
# Check if model is loaded in Foundry Local
foundry model list

# Test API response
curl -X GET http://localhost:51211/v1/models \
  -H "Content-Type: application/json"

# Verify correct port (should be 51211 for Foundry Local)
netstat -ano | findstr :51211
```

**修复**：确保模型已正确加载：
```cmd
# Stop and restart model
foundry model stop phi-4-mini
foundry model run phi-4-mini

# Wait for model to fully load, then refresh Open WebUI
```

### Docker 网络问题

**问题**：`host.docker.internal` 无法解析

**Windows 解决方案**：
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

**替代方案**：找到您的机器 IP：
```cmd
ipconfig | findstr IPv4
# Use your actual IP instead of host.docker.internal
# Example: http://192.168.1.100:51211/v1
```

### 性能问题

**响应缓慢**：
1. 检查模型是否使用 GPU 加速：`foundry service ps`
2. 验证系统资源是否充足（RAM/GPU 内存）
3. 考虑使用较小的模型进行测试

**内存问题**：
```cmd
# Check Docker container memory usage
docker stats open-webui

# Restart Docker if needed
docker restart open-webui
```

## 使用指南

### 基本聊天

1. **选择模型**：从下拉菜单中选择 Foundry Local 模型
2. **输入消息**：使用底部的文本输入框
3. **发送**：按 Enter 或点击发送按钮
4. **查看响应**：实时查看流式响应

### 高级功能

**文件上传**：
1. 点击回形针图标
2. 上传文档（PDF、TXT 等）
3. 提问有关内容的问题
4. 模型将根据文档进行分析并响应

**自定义系统提示**：
1. 设置 → 个性化
2. 设置自定义系统提示
3. 创建一致的 AI 个性/行为

**对话管理**：
- **新聊天**：点击 "+" 开始新的对话
- **聊天历史**：从侧边栏访问之前的对话
- **导出**：将聊天记录下载为文本/JSON

**模型比较**：
1. 在多个浏览器标签页中打开同一个 Open WebUI
2. 在每个标签页中选择不同的模型
3. 对同一提示进行响应比较

### 集成模式

**开发工作流**：
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

## 生产部署

### 安全设置

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

### 多用户设置

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

### 监控和日志记录

```cmd
# View real-time logs
docker logs -f open-webui

# Monitor container resources
docker stats open-webui

# Check container health
docker inspect open-webui | grep -i health
```

## 清理

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

## 后续步骤

### 增强建议

1. **自定义模型**：将您自己的微调模型添加到 Foundry Local
2. **API 集成**：通过 Open WebUI 功能连接到外部 API
3. **文档处理**：设置高级 RAG 管道
4. **多模态**：配置视觉模型进行图像分析

### 扩展考虑

- **负载均衡**：在反向代理后运行多个 Foundry Local 实例
- **模型路由**：针对不同用例使用不同模型
- **资源管理**：优化 GPU 内存以支持并发用户
- **备份策略**：定期备份对话数据和配置

## 参考资料

- [Open WebUI 文档](https://docs.openwebui.com/)
- [Open WebUI GitHub 仓库](https://github.com/open-webui/open-webui)
- [Foundry Local 文档](https://learn.microsoft.com/azure/ai-foundry/foundry-local/)
- [Docker 安装指南](https://docs.docker.com/get-docker/)

---


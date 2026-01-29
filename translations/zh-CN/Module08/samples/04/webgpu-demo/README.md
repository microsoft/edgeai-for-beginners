# WebGPU + ONNX Runtime 演示

此演示展示了如何使用 WebGPU 进行硬件加速和 ONNX Runtime Web，在浏览器中直接运行 AI 模型。

## 演示内容

- **基于浏览器的 AI**：完全在浏览器中运行模型
- **WebGPU 加速**：在支持的情况下进行硬件加速推理
- **隐私优先**：数据不会离开您的设备
- **零安装**：在任何兼容的浏览器中运行
- **优雅降级**：如果 WebGPU 不可用，则回退到 CPU

## 要求

**浏览器兼容性：**
- Chrome/Edge 113+，需启用 WebGPU
- 检查 WebGPU 状态：`chrome://gpu`
- 启用 WebGPU：`chrome://flags/#enable-unsafe-webgpu`

## 运行演示

### 选项 1：本地服务器（推荐）

```cmd
# Navigate to the demo directory
cd Module08\samples\04\webgpu-demo

# Start a local server
python -m http.server 5173

# Open browser to http://localhost:5173
```

### 选项 2：VS Code Live Server

1. 在 VS Code 中安装 "Live Server" 扩展
2. 右键点击 `index.html` → "Open with Live Server"
3. 演示会自动在浏览器中打开

## 您将看到的内容

1. **WebGPU 检测**：检查浏览器兼容性
2. **模型加载**：下载并初始化 MNIST 分类器
3. **推理执行**：对样本数据进行预测
4. **性能指标**：显示加载时间和推理速度
5. **结果展示**：预测置信度和原始输出

## 预期性能

| 执行提供者       | 模型加载 | 推理速度 | 备注               |
|-------------------|----------|----------|--------------------|
| **WebGPU**        | ~2-5秒   | ~10-50毫秒 | 硬件加速           |
| **CPU (WASM)**    | ~2-5秒   | ~50-200毫秒 | 软件回退           |

## 故障排除

**WebGPU 不可用：**
- 更新到 Chrome/Edge 113+
- 在 `chrome://flags` 中启用 WebGPU
- 检查 GPU 驱动是否为最新版本
- 演示会自动回退到 CPU

**加载错误：**
- 确保通过 HTTP 提供服务（而不是 file://）
- 检查网络连接以下载模型
- 验证 CORS 是否阻止了 ONNX 模型

**性能问题：**
- WebGPU 比 CPU 提供显著的加速
- 第一次运行可能较慢，因为需要下载模型
- 后续运行会使用浏览器缓存

## 与 Foundry Local 的集成

此 WebGPU 演示通过以下方式补充了 Foundry Local：

- **客户端推理**，实现终极隐私
- **离线功能**，在无网络时可用  
- **边缘部署**，适用于资源受限的环境
- **混合架构**，结合本地和服务器推理

对于生产应用，建议：
- 使用 Foundry Local 进行服务器端推理
- 使用 WebGPU 进行客户端预处理/后处理
- 实现本地/远程推理之间的智能路由

## 技术细节

**使用的模型：**
- MNIST 数字分类器（ONNX 格式）
- 输入：28x28 灰度图像
- 输出：10 类概率分布
- 大小：约 500KB（快速下载）

**ONNX Runtime Web：**
- WebGPU 执行提供者，用于 GPU 加速
- WASM 执行提供者，用于 CPU 回退
- 自动优化和图优化

**浏览器 API：**
- WebGPU，用于硬件访问
- Web Workers，用于后台处理（未来增强）
- WebAssembly，用于高效计算

## 下一步

- 尝试使用自定义 ONNX 模型
- 实现真实图像上传和分类
- 添加流式推理以支持更大的模型
- 集成摄像头/麦克风输入

---


# Friday - AI 命令行助手

基于 DeepSeek 和 AgentScope 开发的智能命令行助手，支持实时流式输出。

## 功能特性

- ⚡ **实时流式响应** - AI 回复即时显示，无需等待
- 💬 支持多轮对话
- 🤖 采用 DeepSeek 大语言模型
- 🎯 基于 AgentScope 2.0 框架
- 🔒 使用环境变量安全管理 API 密钥
- 🌐 完整支持中文交互

## 安装步骤

### 1. 创建虚拟环境（推荐）

使用虚拟环境可以隔离项目依赖，避免与系统 Python 包冲突：

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
# macOS/Linux:
source venv/bin/activate

# Windows:
# venv\Scripts\activate
```

激活后，命令行提示符前会显示 `(venv)`。

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

复制 `.env.example` 为 `.env` 并添加你的 DeepSeek API 密钥：

```bash
cp .env.example .env
```

编辑 `.env` 文件并设置你的 API 密钥：

```
DEEPSEEK_API_KEY=你的实际API密钥
```

## 使用方法

### 标准运行方式

```bash
python main.py
```

### Apple Silicon (M1/M2/M3) 用户

如果遇到架构兼容性问题，请使用 ARM64 模式：

```bash
arch -arm64 python3 main.py
```

或使用提供的启动脚本：

```bash
./run.sh
```

### 添加可执行权限（可选）

```bash
chmod +x main.py
./main.py
```

输入 `exit` 或 `quit` 退出对话。

### 退出虚拟环境

当你完成工作后，可以退出虚拟环境：

```bash
deactivate
```

## 使用示例

```
You: 你好，Friday！
Friday: 你好！我能为你做些什么？

You: 请介绍一下Python的特点
Friday: [AI 实时流式输出响应，逐字显示...]

You: exit
Friday: Goodbye! Have a great day!
```

## 技术细节

### 流式输出实现

Friday 使用 AgentScope 2.0 的 `reply_stream()` 方法实现实时流式响应：

- 处理 `TextBlockDeltaEvent` 事件进行增量文本输出
- 使用 async/await 实现高效事件处理
- 在 AI 生成响应时提供即时的视觉反馈

### 项目架构

- **Agent 框架**: AgentScope 2.0
- **LLM 提供商**: DeepSeek API (OpenAI 兼容)
- **异步运行时**: Python asyncio
- **优化**: 支持 ARM64 架构

## 依赖项

- `agentscope>=2.0.0` - 支持流式输出的 AI agent 框架
- `python-dotenv` - 环境变量管理

## 虚拟环境说明

### 为什么使用虚拟环境？

1. **依赖隔离** - 不同项目的包版本互不影响
2. **避免冲突** - 防止与系统 Python 包产生版本冲突
3. **易于管理** - 可以轻松删除和重建环境
4. **可复现性** - 确保团队成员使用相同的依赖版本

### 虚拟环境管理

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# 安装依赖
pip install -r requirements.txt

# 退出虚拟环境
deactivate

# 删除虚拟环境（如需重建）
rm -rf venv
```

### 注意事项

- `venv/` 目录已添加到 `.gitignore`，不会提交到版本控制
- 每次打开新终端窗口都需要重新激活虚拟环境
- 推荐在项目根目录创建虚拟环境

## 故障排查

### Mac 上的架构问题

如果遇到架构兼容性错误：
```bash
arch: posix_spawnp: python: Bad CPU type in executable
```

解决方案：显式使用 ARM64 模式：
```bash
arch -arm64 python3 main.py
```

### 流式输出不工作

请确保：
- 使用 AgentScope 2.0 或更高版本
- Python 3.8 或更高版本
- DeepSeek API 密钥有效

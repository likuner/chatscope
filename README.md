# Friday - AI 命令行助手

基于多种大语言模型和 AgentScope 开发的智能命令行助手，支持实时流式输出。

## 功能特性

- ⚡ **实时流式响应** - AI 回复即时显示，无需等待
- 💬 支持多轮对话
- 🤖 支持多种大语言模型：Qwen、DeepSeek、GLM
- 🔄 **一键切换模型** - 修改配置即可切换不同的 AI 模型
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

复制 `.env.example` 为 `.env` 并配置你的 API 密钥：

```bash
cp .env.example .env
```

然后编辑 `.env` 文件，根据你要使用的模型进行配置。详细配置说明请查看下方的[环境变量配置指南](#环境变量配置指南)。

## 环境变量配置指南

### 配置文件结构

`.env` 文件包含以下几类配置：

#### 1. 模型提供商选择 (必填)

指定要使用哪个大模型：

```bash
MODEL_PROVIDER=deepseek
```

**可选值：**
- `qwen` - 使用通义千问
- `deepseek` - 使用 DeepSeek
- `glm` - 使用智谱 AI

#### 2. 各模型的 API 配置

根据你选择的 `MODEL_PROVIDER`，配置对应模型的参数：

##### Qwen (通义千问)

```bash
QWEN_API_KEY=sk-xxxxxxxxxxxxxx          # 必填：你的 API 密钥
QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1  # 可选：API 地址
QWEN_MODEL_NAME=qwen-max                # 可选：模型名称
```

- **API 密钥获取**：访问 [阿里云百炼平台](https://bailian.console.aliyun.com/)
- **可用模型**：`qwen-max`（推荐）、`qwen-plus`、`qwen-turbo`

##### DeepSeek

```bash
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxx      # 必填：你的 API 密钥
DEEPSEEK_BASE_URL=https://api.deepseek.com  # 可选：API 地址
DEEPSEEK_MODEL_NAME=deepseek-chat       # 可选：模型名称
```

- **API 密钥获取**：访问 [DeepSeek 开放平台](https://platform.deepseek.com/)
- **可用模型**：`deepseek-chat`（推荐）、`deepseek-coder`

##### GLM (智谱 AI)

```bash
GLM_API_KEY=xxxxxxxxxxxxxx.xxxxxxxxxxxxx  # 必填：你的 API 密钥
GLM_BASE_URL=https://open.bigmodel.cn/api/paas/v4  # 可选：API 地址
GLM_MODEL_NAME=glm-4-plus               # 可选：模型名称
```

- **API 密钥获取**：访问 [智谱 AI 开放平台](https://open.bigmodel.cn/)
- **可用模型**：`glm-4-plus`（推荐）、`glm-4`、`glm-4-flash`

#### 3. 模型参数 (可选)

这些参数对所有模型生效：

```bash
TEMPERATURE=0.7      # 温度参数 (0.0-1.0)，越高输出越随机
MAX_TOKENS=2048      # 单次回复的最大 token 数
```

### 完整配置示例

#### 示例 1: 使用 DeepSeek（推荐新手）

```bash
MODEL_PROVIDER=deepseek
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxx
```

其他参数使用默认值即可。

#### 示例 2: 使用 Qwen 并自定义参数

```bash
MODEL_PROVIDER=qwen
QWEN_API_KEY=sk-xxxxxxxxxxxxxx
QWEN_MODEL_NAME=qwen-plus
TEMPERATURE=0.8
MAX_TOKENS=4096
```

#### 示例 3: 配置所有模型（方便切换）

```bash
# 当前使用的模型
MODEL_PROVIDER=deepseek

# Qwen 配置
QWEN_API_KEY=sk-xxxxxxxxxxxxxx
QWEN_MODEL_NAME=qwen-max

# DeepSeek 配置
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxx
DEEPSEEK_MODEL_NAME=deepseek-chat

# GLM 配置
GLM_API_KEY=xxxxxxxxxxxxxx.xxxxxxxxxxxxx
GLM_MODEL_NAME=glm-4-plus

# 全局参数
TEMPERATURE=0.7
MAX_TOKENS=2048
```

配置所有模型后，只需修改 `MODEL_PROVIDER` 即可快速切换。

### 配置注意事项

1. **API 密钥格式**
   - Qwen 和 DeepSeek：通常以 `sk-` 开头
   - GLM：格式为 `xxxxxxxx.xxxxxxxx`（包含一个点）

2. **只需配置使用的模型**
   - 如果只用 DeepSeek，只需配置 `DEEPSEEK_API_KEY`
   - 未使用的模型配置可以留空

3. **安全提醒**
   - ⚠️ 不要将 `.env` 文件提交到 Git
   - ⚠️ 不要在公开场合分享你的 API 密钥
   - ✅ `.env` 已添加到 `.gitignore`

4. **BASE_URL 修改场景**
   - 一般情况下使用默认值
   - 需要使用代理或私有部署时才需要修改

## 模型切换指南

### 快速切换模型

只需修改 `.env` 文件中的 `MODEL_PROVIDER` 参数：

```bash
# 使用 Qwen
MODEL_PROVIDER=qwen

# 使用 DeepSeek
MODEL_PROVIDER=deepseek

# 使用 GLM
MODEL_PROVIDER=glm
```

修改后重新运行程序即可切换到对应的模型，无需修改任何代码。

### 支持的模型详情

#### 1. **Qwen (通义千问)** - 阿里云
- **API 获取**：[阿里云百炼平台](https://dashscope.aliyuncs.com/)
- **默认模型**：`qwen-max` (最新最强版本)
- **可选模型**：
  - `qwen-max` - 性能最强，适合复杂任务
  - `qwen-plus` - 平衡性能与成本
  - `qwen-turbo` - 速度最快，成本最低
- **特点**：中文理解优秀，响应速度快

#### 2. **DeepSeek** - DeepSeek AI
- **API 获取**：[DeepSeek 开放平台](https://platform.deepseek.com/)
- **默认模型**：`deepseek-chat` (最新版本)
- **可选模型**：
  - `deepseek-chat` - 通用对话模型
  - `deepseek-coder` - 专注代码生成
- **特点**：性价比高，代码能力强

#### 3. **GLM (智谱AI)** - 清华系
- **API 获取**：[智谱AI开放平台](https://open.bigmodel.cn/)
- **默认模型**：`glm-4-plus` (最新增强版本)
- **可选模型**：
  - `glm-4-plus` - 增强版本，性能更强
  - `glm-4` - 标准版本
  - `glm-4-flash` - 快速响应版本
- **特点**：国产大模型，中文能力优秀

### 自定义模型参数

你可以在 `.env` 文件中灵活调整各个模型的配置：

#### 修改模型名称

根据需求选择不同的模型版本：

```bash
# Qwen - 选择性能更强的版本
QWEN_MODEL_NAME=qwen-max

# DeepSeek - 使用代码专用模型
DEEPSEEK_MODEL_NAME=deepseek-coder

# GLM - 使用快速响应版本
GLM_MODEL_NAME=glm-4-flash
```

#### 调整生成参数

```bash
# 温度参数 (0.0-1.0)
# - 0.0-0.3: 输出更确定、保守，适合事实性问答
# - 0.4-0.7: 平衡创造性和准确性（推荐）
# - 0.8-1.0: 输出更随机、创造性，适合创意写作
TEMPERATURE=0.7

# 最大 Token 数 (控制回复长度)
# - 512-1024: 简短回复
# - 2048: 标准长度（推荐）
# - 4096-8192: 长篇回复
MAX_TOKENS=2048
```

#### 修改 API 地址

一般情况下不需要修改，以下场景可能需要：

```bash
# 使用代理服务
DEEPSEEK_BASE_URL=https://your-proxy.com/v1

# 使用私有部署
QWEN_BASE_URL=https://your-private-endpoint.com
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
Friday - Your AI Assistant (Using DEEPSEEK)
============================================================
Type 'exit' or 'quit' to end the conversation.

🍭 You: 你好，Friday！
🚀 Friday: 你好！我能为你做些什么？

🍭 You: 请介绍一下Python的特点
🚀 Friday: [AI 实时流式输出响应，逐字显示...]

🍭 You: exit

✨ Friday: Goodbye! Have a great day!
```

**注意**：程序启动时会显示当前使用的模型提供商（QWEN、DEEPSEEK 或 GLM）。

## 技术细节

### 流式输出实现

Friday 使用 AgentScope 2.0 的 `reply_stream()` 方法实现实时流式响应：

- 处理 `TextBlockDeltaEvent` 事件进行增量文本输出
- 使用 async/await 实现高效事件处理
- 在 AI 生成响应时提供即时的视觉反馈

### 项目架构

- **Agent 框架**: AgentScope 2.0
- **支持的 LLM 提供商**: 
  - Qwen (通义千问) - 阿里云
  - DeepSeek - DeepSeek API
  - GLM (智谱AI) - 智谱开放平台
- **异步运行时**: Python asyncio
- **配置管理**: pydantic-settings + python-dotenv
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
- API 密钥有效且配置正确

### 模型无法连接

检查以下内容：
1. 确认 `.env` 文件中的 `MODEL_PROVIDER` 设置正确
2. 确认对应模型的 API 密钥已正确配置
3. 检查网络连接是否正常
4. 验证 API 密钥是否有效且有足够的额度

### 配置文件错误

如果提示配置错误：
```bash
# 确保 .env 文件存在
ls -la .env

# 如果不存在，从示例文件复制
cp .env.example .env
```

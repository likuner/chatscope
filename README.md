# Friday - AI 命令行助手

基于多种大语言模型和 AgentScope 开发的智能命令行助手，支持实时流式输出。

## ✨ 功能特性

- ⚡ **实时流式响应** - AI 回复即时显示，无需等待
- 💬 **多轮对话** - 保持上下文的连续对话
- 🤖 **多模型支持** - Qwen、DeepSeek、GLM 任意切换
- 🔄 **零代码切换** - 修改环境变量即可切换模型
- 📝 **完整日志** - 记录每一步对话过程，方便调试
- 🔒 **安全管理** - 使用环境变量保护 API 密钥
- 🌐 **中文优化** - 完整支持中文交互

## 🚀 快速开始

### 1. 克隆项目并安装

```bash
# 创建虚拟环境（推荐，隔离依赖）
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置 API 密钥

```bash
# 复制配置文件
cp .env.example .env

# 编辑 .env 文件，至少配置以下两项：
# MODEL_PROVIDER=deepseek              # 选择模型: qwen/deepseek/glm
# DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxx   # 对应模型的 API 密钥
```

### 3. 运行

```bash
python3 main.py
# Apple Silicon 用户如遇问题可使用: arch -arm64 python3 main.py
```

输入 `exit` 或 `quit` 退出对话。

## ⚙️ 配置指南

### 支持的模型

| 模型 | 提供商 | 获取 API | 特点 |
|------|--------|----------|------|
| **Qwen** | 阿里云 | [百炼平台](https://bailian.console.aliyun.com/) | 中文理解优秀，响应快 |
| **DeepSeek** | DeepSeek | [开放平台](https://platform.deepseek.com/) | 性价比高，代码能力强 |
| **GLM** | 智谱 AI | [开放平台](https://open.bigmodel.cn/) | 国产大模型，中文优秀 |

### 配置文件说明

`.env` 文件包含以下配置项：

#### 必填项

```bash
# 选择使用的模型 (必填)
MODEL_PROVIDER=deepseek  # 可选: qwen, deepseek, glm

# 对应模型的 API 密钥 (必填)
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxx
```

#### 可选项

```bash
# 各模型的 Base URL（一般不需要修改）
QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
DEEPSEEK_BASE_URL=https://api.deepseek.com
GLM_BASE_URL=https://open.bigmodel.cn/api/paas/v4

# 各模型的模型名称
QWEN_MODEL_NAME=qwen-max           # 可选: qwen-max, qwen-plus, qwen-turbo
DEEPSEEK_MODEL_NAME=deepseek-chat  # 可选: deepseek-chat, deepseek-coder
GLM_MODEL_NAME=glm-4-plus          # 可选: glm-4-plus, glm-4, glm-4-flash

# 生成参数（所有模型通用）
TEMPERATURE=0.7    # 0.0-1.0, 越高越随机
MAX_TOKENS=2048    # 单次回复的最大长度
```

### 配置示例

#### 最简配置（推荐新手）

只配置你要使用的模型：

```bash
MODEL_PROVIDER=deepseek
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxx
```

#### 完整配置（方便切换）

配置所有模型，通过修改 `MODEL_PROVIDER` 快速切换：

```bash
MODEL_PROVIDER=deepseek

QWEN_API_KEY=sk-xxxxxxxxxxxxxx
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxx
GLM_API_KEY=xxxxxxxxxxxxxx.xxxxxxxxxxxxx

TEMPERATURE=0.7
MAX_TOKENS=2048
```

### 重要提示

- ⚠️ **API 密钥格式**：Qwen/DeepSeek 以 `sk-` 开头，GLM 格式为 `xxx.xxx`（含一个点）
- ⚠️ **不要泄露密钥**：`.env` 已在 `.gitignore` 中，不会提交到 Git
- ✅ **只需配置使用的模型**：未使用的模型配置可以留空

## 💡 使用示例

```
Friday - Your AI Assistant (Using DEEPSEEK)
============================================================
Type 'exit' or 'quit' to end the conversation.

🍭 You: 你好，Friday！
🚀 Friday: 你好！我能为你做些什么？

🍭 You: 请介绍一下Python的特点
🚀 Friday: Python 是一种高级编程语言，具有以下特点...
          [AI 实时流式输出响应，逐字显示]

🍭 You: exit
✨ Friday: Goodbye! Have a great day!
```

## 🔧 调试功能

项目内置完整的日志记录功能，记录每一步对话过程：

```bash
# 运行程序（自动记录日志到 friday.log）
python3 main.py

# 实时查看日志
tail -f friday.log

# 查看特定对话
grep "对话 #1" friday.log
```

日志包含：
- 配置加载过程
- 模型初始化
- 每次对话的用户输入和 AI 响应
- 事件处理详情和错误信息

还可以使用调试脚本测试配置：

```bash
# 测试配置是否正确
python3 debug_config.py
```

## 📚 技术架构

- **Agent 框架**: AgentScope 2.0 - 支持流式输出
- **LLM 支持**: Qwen (阿里云) / DeepSeek / GLM (智谱 AI)
- **异步处理**: Python asyncio
- **配置管理**: pydantic-settings + python-dotenv
- **架构优化**: 支持 ARM64 (Apple Silicon)

### 流式输出实现

使用 AgentScope 2.0 的 `reply_stream()` 方法实现实时响应：
- 处理 `TextBlockDeltaEvent` 事件进行增量输出
- 使用 async/await 实现高效事件处理
- 在生成过程中提供即时的视觉反馈

## 🛠️ 故障排查

### 常见问题

| 问题 | 解决方案 |
|------|----------|
| **架构兼容性错误** (Mac) | 使用 `arch -arm64 python3 main.py` 或运行 `./run.sh` |
| **流式输出不工作** | 确保 AgentScope >= 2.0，Python >= 3.8 |
| **模型无法连接** | 检查 `MODEL_PROVIDER` 设置、API 密钥、网络连接 |
| **配置文件错误** | 确认 `.env` 存在，可用 `python3 debug_config.py` 测试 |
| **导入错误** | 确认已激活虚拟环境：`source venv/bin/activate` |

### 调试步骤

1. **测试配置**
```bash
python3 debug_config.py
```

2. **查看日志**
```bash
tail -f friday.log
```

3. **检查虚拟环境**
```bash
which python3  # 应显示 venv/bin/python3
pip list       # 查看已安装的包
```

## 📖 项目文件说明

```
chatscope/
├── main.py              # 主程序入口
├── config.py            # 配置管理（支持多模型）
├── debug_config.py      # 配置测试工具
├── requirements.txt     # Python 依赖
├── .env.example         # 配置文件模板
├── .env                 # 实际配置（不提交到 Git）
├── run.sh              # 启动脚本（Apple Silicon 优化）
├── friday.log          # 日志文件（自动生成）
└── README.md           # 项目文档
```

## 💪 虚拟环境管理

### 常用命令

```bash
# 激活虚拟环境
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# 退出虚拟环境
deactivate

# 更新依赖
pip install --upgrade -r requirements.txt

# 重建虚拟环境（如遇问题）
deactivate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 为什么使用虚拟环境？

- ✅ **依赖隔离** - 不同项目互不影响
- ✅ **避免冲突** - 防止版本冲突
- ✅ **易于管理** - 可轻松删除和重建
- ✅ **可复现性** - 团队使用相同依赖版本

## 📝 开发日志

- **v1.0** - 初始版本，支持 Qwen
- **v1.1** - 添加 DeepSeek 和 GLM 支持
- **v1.2** - 实现多模型配置系统
- **v1.3** - 添加完整日志记录功能
- **v1.4** - 优化文档和调试工具

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

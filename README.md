# XeeAIStu - AI 智能内容创作平台

基于多模型 AI 引擎的内容创作工具，支持自动生成技术博客、产品文案与 SEO 优化文章。

## 功能特性

- **多模型 AI 驱动**：集成 OpenAI、Gemini 等主流大模型，可灵活切换
- **智能标题生成**：输入主题，自动生成多个 SEO 优化标题
- **一键内容创作**：自动生成结构化 Markdown 文章，包含 Meta 描述和标签
- **竞争对手分析**：自动发现竞品，生成对比文章
- **灵活导出**：支持 Markdown / HTML 复制、PDF 导出

## 技术栈

Python · Django 5 · Django REST Framework · PostgreSQL · Redis · Docker · OpenAI API · Gemini API

## 快速开始

### 1. 环境准备

```bash
# 克隆项目
git clone https://github.com/rasulkireev/tuxseo.git
cd tuxseo

# 复制环境变量配置文件
cp .env.example .env
```

### 2. 配置 API 密钥

编辑 `.env` 文件，填入以下必填的 API 密钥：

| 变量 | 说明 | 获取地址 |
|------|------|---------|
| `OPENAI_API_KEY` | OpenAI API 密钥 | https://platform.openai.com/api-keys |
| `GEMINI_API_KEY` | Gemini API 密钥 | https://aistudio.google.com/app/apikey |
| `TAVILY_API_KEY` | Tavily 搜索 API | https://tavily.com/ |
| `JINA_READER_API_KEY` | Jina Reader API | https://jina.ai/reader/ |
| `PERPLEXITY_API_KEY` | Perplexity API | https://perplexity.ai/ |
| `KEYWORDS_EVERYWHERE_API_KEY` | Keywords Everywhere | https://keywordseverywhere.com/ |

### 3. 启动服务

```bash
# 启动所有服务（Docker Compose）
make serve

# 如果 Worker 首次连接 Redis 异常，重启 Worker
make restart-worker
```

启动后访问：
- 后端：http://localhost:8009
- 前端：http://localhost:9093
- MailHog（邮件调试）：http://localhost:8025

## 部署

### Render 一键部署

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/rasulkireev/tuxseo)

> **注意**：免费套餐可满足基本使用，但后台自动化任务（批量分析、生成）可能因 512MB 内存限制而失败。手动操作（如生成单篇文章）不受影响。

### Docker Compose 部署

在服务器上准备两个文件：

1. `.env` — 复制 `.env.example` 并填入所有必要配置
2. `docker-compose.yml` — 复制 `docker-compose-prod.yml` 内容，按文件顶部注释中的命令启动

### CapRover 部署

1. 在 CapRover 上创建 4 个应用：`xeeaistu`、`xeeaistu-workers`、`xeeaistu-postgres`、`xeeaistu-redis`
2. 为 `xeeaistu` 和 `xeeaistu-workers` 创建 App Token
3. 根据 `.env` 配置环境变量
4. 配置 GitHub Actions Secrets（`CAPROVER_SERVER`、`CAPROVER_APP_TOKEN` 等）
5. 推送代码到 main 分支，GitHub Workflow 自动完成部署

## 本地开发

### 运行测试

```bash
# 运行完整测试套件（与 CI 一致）
make test-ci

# 运行内容质量评估测试
make test-content-quality
```

### 进入 Django Shell

```bash
make shell
```

### 数据库迁移

```bash
make makemigrations
make manage migrate
```

## 项目结构

| 目录 / 文件 | 说明 |
|------------|------|
| `core/` | 核心业务逻辑：模型、视图、任务、API |
| `frontend/` | 前端资源：模板、Webpack 打包配置 |
| `tuxseo/` | Django 项目配置、URL 路由 |
| `deployment/` | 部署相关脚本 |
| `scripts/` | 运维工具脚本 |
| `docs/` | 项目文档 |
| `docker-compose-local.yml` | 本地开发 Docker 编排 |
| `docker-compose-prod.yml` | 生产环境 Docker 编排 |
| `Dockerfile-python` | Python 后端镜像 |
| `Makefile` | 常用命令快捷入口 |

## 内部 API

内部博客文章管理接口位于 `/api/internal/blog-posts`，需通过超级用户 API Key 认证（`?api_key=...`）：

- `POST /api/blog-posts/submit` — 创建文章
- `GET /api/internal/blog-posts` — 文章列表
- `GET /api/internal/blog-posts/{id}` — 文章详情
- `PUT /api/internal/blog-posts/{id}` — 完整更新
- `PATCH /api/internal/blog-posts/{id}` — 部分更新
- `DELETE /api/internal/blog-posts/{id}` — 删除文章

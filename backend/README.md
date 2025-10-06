# 原声雷达 - 后端 API

基于 FastAPI 的高性能后端服务。

## 安装依赖

### 使用 uv（推荐）

```bash
uv pip install -e .
```

### 使用 pip

```bash
pip install -e .
```

## 运行服务

```bash
uvicorn main:app --reload --port 8000
```

## API 文档

启动服务后访问：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 项目结构

- `main.py` - FastAPI 应用主文件，包含所有路由
- `models.py` - Pydantic 数据模型定义
- `mock_data.py` - 模拟数据生成器

## 模拟数据

系统自动生成：
- 5个模拟用户
- 每个用户 12-18 条帖子
- 每条帖子 0-8 条评论

数据主题围绕中国安卓手机用户反馈。


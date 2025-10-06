# 原声雷达 - 安卓手机用户反馈社区

一个基于 Vue3 + FastAPI 的现代化社区平台，专注于中国安卓手机用户的反馈与交流。

## 📱 项目特点

- 🎨 **现代化 UI** - 卡片式设计，类似小红书的信息流布局
- 📱 **响应式布局** - 完美适配 PC 端和移动端 H5
- ⚡ **高性能** - 无限下拉加载，流畅的用户体验
- 🎯 **功能完整** - 信息流、帖子详情、个人主页、评论系统

## 🛠 技术栈

### 前端
- **Vue 3** - 渐进式 JavaScript 框架
- **Vite** - 下一代前端构建工具
- **Pinia** - Vue 3 状态管理
- **Vue Router** - 官方路由管理器
- **Axios** - HTTP 客户端

### 后端
- **FastAPI** - 现代化、高性能的 Python Web 框架
- **Pydantic** - 数据验证和设置管理
- **uvicorn** - ASGI 服务器

## 📦 项目结构

```
Vocal-Radar-Workspace/
├── frontend/                # 前端项目
│   ├── src/
│   │   ├── api/            # API 接口
│   │   ├── components/     # Vue 组件
│   │   ├── views/          # 页面视图
│   │   ├── stores/         # Pinia 状态管理
│   │   ├── router/         # 路由配置
│   │   ├── App.vue         # 根组件
│   │   └── main.js         # 入口文件
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
└── backend/                 # 后端项目
    ├── main.py             # FastAPI 主应用
    ├── models.py           # 数据模型
    ├── mock_data.py        # 模拟数据
    └── pyproject.toml      # 依赖配置
```

## 🚀 快速开始

### 前置要求

- Node.js >= 16
- Python >= 3.9
- uv (推荐) 或 pip

### 安装 uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 后端启动

```bash
# 进入后端目录
cd backend

# 使用 uv 安装依赖
uv pip install -e .

# 或使用传统 pip
# pip install -e .

# 启动后端服务
uvicorn main:app --reload --port 8000
```

后端服务将运行在 `http://localhost:8000`

API 文档：`http://localhost:8000/docs`

### 前端启动

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

前端服务将运行在 `http://localhost:3000`

## 📡 API 接口

### 帖子相关

- `GET /posts` - 获取帖子列表（支持分页）
  - 参数：`page`, `page_size`, `user_id`
- `GET /posts/{post_id}` - 获取帖子详情

### 用户相关

- `GET /users/{user_id}` - 获取用户详情
- `GET /users/{user_id}/posts` - 获取用户的帖子
- `GET /random-user` - 获取随机模拟用户

### 评论相关

- `GET /comments?post_id={post_id}` - 获取帖子评论

## 🎯 核心功能

### 1. 信息流首页
- ✅ 无限下拉加载
- ✅ 帖子卡片展示（标题、内容、图片/视频、作者信息）
- ✅ 支持多图和视频显示
- ✅ 点击雷达图标刷新

### 2. 帖子详情页
- ✅ 完整内容展示
- ✅ 图片点击查看
- ✅ 视频播放
- ✅ 评论列表

### 3. 个人主页
- ✅ 用户信息展示
- ✅ 用户帖子列表
- ✅ 统计信息

### 4. 用户体系
- ✅ 5个模拟用户
- ✅ 自动随机分配身份
- ✅ 本地持久化

## 🎨 界面特点

- **卡片式设计** - 现代化的卡片布局
- **雷达图标** - 可点击的旋转雷达动画
- **响应式布局** - PC 和移动端完美适配
- **流畅动画** - 悬停效果和过渡动画
- **优雅交互** - 点赞、评论、跳转等交互

## 📱 移动端适配

- 自适应布局，在各种屏幕尺寸下都有良好表现
- 触摸友好的交互设计
- 优化的图片和视频加载

## 🔧 开发建议

### 扩展功能
- 添加搜索功能
- 实现真实的用户认证
- 添加帖子发布功能
- 实现点赞和评论交互
- 添加图片预览组件

### 性能优化
- 实现虚拟滚动
- 图片懒加载
- 组件按需加载
- 接口缓存

## 📝 模拟数据

- **用户数**: 5个模拟用户
- **帖子数**: 每用户 12-18 条帖子（总计约 60-90 条）
- **评论数**: 每帖子 0-8 条随机评论
- **主题**: 中国安卓手机用户反馈（信号、续航、拍照、系统等）

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 License

MIT License

## 📧 联系方式

如有问题，请通过 Issue 联系我们。

---

**原声雷达** - 让每一个声音都被听见 📡


#!/bin/bash

# 原声雷达环境安装脚本

echo "🔧 开始安装原声雷达环境..."
echo ""

# 检查 Node.js
if ! command -v node &> /dev/null; then
    echo "❌ 未检测到 Node.js，请先安装 Node.js (>= 16)"
    exit 1
fi

echo "✅ Node.js 版本: $(node --version)"
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 未检测到 Python 3，请先安装 Python (>= 3.9)"
    exit 1
fi

echo "✅ Python 版本: $(python3 --version)"
echo ""

# 安装 uv（可选）
echo "📦 检查 uv..."
if ! command -v uv &> /dev/null; then
    echo "⚠️  未检测到 uv，推荐安装 uv 作为包管理器"
    echo "   安装命令: curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo "   或者使用传统的 pip 也可以"
    echo ""
fi

# 安装后端依赖
echo "📦 安装后端依赖..."
cd backend

if command -v uv &> /dev/null; then
    echo "使用 uv 安装..."
    uv pip install -e .
else
    echo "使用 pip 安装..."
    pip3 install -e .
fi

if [ $? -eq 0 ]; then
    echo "✅ 后端依赖安装完成"
else
    echo "❌ 后端依赖安装失败"
    exit 1
fi

cd ..
echo ""

# 安装前端依赖
echo "📦 安装前端依赖..."
cd frontend
npm install

if [ $? -eq 0 ]; then
    echo "✅ 前端依赖安装完成"
else
    echo "❌ 前端依赖安装失败"
    exit 1
fi

cd ..
echo ""

# 设置权限
chmod +x start.sh

echo "🎉 环境安装完成！"
echo ""
echo "运行以下命令启动服务："
echo "  ./start.sh"
echo ""
echo "或者分别启动："
echo "  后端: cd backend && uvicorn main:app --reload --port 8000"
echo "  前端: cd frontend && npm run dev"


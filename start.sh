#!/bin/bash

# 原声雷达启动脚本

echo "🚀 启动原声雷达..."
echo ""

# 检查是否已安装依赖
if [ ! -d "frontend/node_modules" ]; then
    echo "📦 正在安装前端依赖..."
    cd frontend && npm install && cd ..
    echo "✅ 前端依赖安装完成"
    echo ""
fi

# 启动后端
echo "🔧 启动后端服务..."
cd backend
uvicorn main:app --reload --port 8000 &
BACKEND_PID=$!
cd ..

# 等待后端启动
sleep 2

# 启动前端
echo "🎨 启动前端服务..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "✅ 服务启动成功！"
echo ""
echo "📡 后端服务: http://localhost:8000"
echo "📚 API 文档: http://localhost:8000/docs"
echo "🎨 前端服务: http://localhost:3000"
echo ""
echo "按 Ctrl+C 停止服务"

# 等待用户中断
wait


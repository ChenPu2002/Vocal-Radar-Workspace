from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from datetime import datetime, timedelta
import random
from models import Post, User, Comment, PostDetail, UserDetail
from mock_data import users, posts, comments

app = FastAPI(title="原声雷达 API")

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "欢迎使用原声雷达 API"}


@app.get("/posts", response_model=dict)
async def get_posts(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
    user_id: Optional[int] = None
):
    """获取帖子列表（分页）"""
    # 筛选用户的帖子
    filtered_posts = posts if user_id is None else [p for p in posts if p.user_id == user_id]
    
    # 排序（按时间倒序）
    sorted_posts = sorted(filtered_posts, key=lambda x: x.created_at, reverse=True)
    
    # 分页
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    page_posts = sorted_posts[start_idx:end_idx]
    
    # 填充用户信息
    result_posts = []
    for post in page_posts:
        user = next((u for u in users if u.id == post.user_id), None)
        post_dict = post.dict()
        if user:
            post_dict["author"] = {
                "id": user.id,
                "nickname": user.nickname,
                "avatar": user.avatar
            }
        result_posts.append(post_dict)
    
    return {
        "total": len(sorted_posts),
        "page": page,
        "page_size": page_size,
        "data": result_posts
    }


@app.get("/posts/{post_id}", response_model=PostDetail)
async def get_post_detail(post_id: int):
    """获取帖子详情"""
    post = next((p for p in posts if p.id == post_id), None)
    if not post:
        return {"error": "帖子不存在"}
    
    user = next((u for u in users if u.id == post.user_id), None)
    post_comments = [c for c in comments if c.post_id == post_id]
    
    # 填充评论的用户信息
    comment_list = []
    for comment in post_comments:
        comment_user = next((u for u in users if u.id == comment.user_id), None)
        comment_dict = comment.dict()
        if comment_user:
            comment_dict["author"] = {
                "id": comment_user.id,
                "nickname": comment_user.nickname,
                "avatar": comment_user.avatar
            }
        comment_list.append(comment_dict)
    
    return PostDetail(
        **post.dict(),
        author={
            "id": user.id,
            "nickname": user.nickname,
            "avatar": user.avatar,
            "bio": user.bio
        } if user else None,
        comments=comment_list
    )


@app.get("/users/{user_id}", response_model=UserDetail)
async def get_user_detail(user_id: int):
    """获取用户详情"""
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        return {"error": "用户不存在"}
    
    user_posts = [p for p in posts if p.user_id == user_id]
    
    return UserDetail(
        **user.dict(),
        post_count=len(user_posts)
    )


@app.get("/users/{user_id}/posts", response_model=dict)
async def get_user_posts(
    user_id: int,
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50)
):
    """获取用户的帖子列表"""
    return await get_posts(page=page, page_size=page_size, user_id=user_id)


@app.get("/comments", response_model=List[dict])
async def get_comments(post_id: int):
    """获取帖子的评论列表"""
    post_comments = [c for c in comments if c.post_id == post_id]
    
    # 填充用户信息
    result_comments = []
    for comment in post_comments:
        user = next((u for u in users if u.id == comment.user_id), None)
        comment_dict = comment.dict()
        if user:
            comment_dict["author"] = {
                "id": user.id,
                "nickname": user.nickname,
                "avatar": user.avatar
            }
        result_comments.append(comment_dict)
    
    return result_comments


@app.get("/random-user", response_model=User)
async def get_random_user():
    """获取一个随机模拟用户（用于前端模拟登录）"""
    return random.choice(users)


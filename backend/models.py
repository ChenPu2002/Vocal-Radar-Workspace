from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class User(BaseModel):
    id: int
    nickname: str
    avatar: str
    bio: str


class UserDetail(User):
    post_count: int


class Post(BaseModel):
    id: int
    user_id: int
    title: str
    content: str
    media_type: str  # "image" or "video" or "none"
    media_urls: List[str]
    likes: int
    comments_count: int
    created_at: datetime


class PostDetail(Post):
    author: Optional[dict] = None
    comments: List[dict] = []


class Comment(BaseModel):
    id: int
    post_id: int
    user_id: int
    content: str
    created_at: datetime


<template>
  <div class="post-detail-container">
    <div v-if="loading" class="loading">加载中...</div>
    
    <div v-else-if="post" class="detail-wrapper">
      <div class="back-btn" @click="goBack">
        <svg class="icon" viewBox="0 0 1024 1024">
          <path d="M724 218.3V141c0-6.7-7.7-10.4-12.9-6.3L260.3 486.8a31.86 31.86 0 0 0 0 50.3l450.8 352.1c5.3 4.1 12.9.4 12.9-6.3v-77.3c0-4.9-2.3-9.6-6.1-12.6l-360-281 360-281.1c3.8-3 6.1-7.7 6.1-12.6z"/>
        </svg>
        返回
      </div>
      
      <div class="post-content">
        <div class="post-header">
          <div class="author-info" @click="goToUser">
            <img :src="post.author.avatar" :alt="post.author.nickname" class="author-avatar" />
            <div class="author-meta">
              <div class="author-name">{{ post.author.nickname }}</div>
              <div class="author-bio">{{ post.author.bio }}</div>
              <div class="post-time">{{ formatTime(post.created_at) }}</div>
            </div>
          </div>
        </div>
        
        <h1 class="post-title">{{ post.title }}</h1>
        
        <div class="post-body">{{ post.content }}</div>
        
        <!-- 图片展示 -->
        <div v-if="post.media_type === 'image' && post.media_urls.length > 0" class="media-section">
          <div 
            v-for="(url, index) in post.media_urls" 
            :key="index"
            class="image-wrapper"
            @click="viewImage(index)"
          >
            <img :src="url" :alt="`图片${index + 1}`" class="post-image" />
          </div>
        </div>
        
        <!-- 视频展示 -->
        <div v-if="post.media_type === 'video' && post.media_urls.length > 0" class="media-section">
          <video :src="post.media_urls[0]" class="post-video" controls></video>
        </div>
        
        <div class="post-stats">
          <div class="stat-item">
            <svg class="icon" viewBox="0 0 1024 1024">
              <path d="M885.9 533.7c16.8-22.2 26.1-49.4 26.1-77.7 0-44.9-25.1-87.4-65.5-111.1a67.67 67.67 0 0 0-34.3-9.3H572.4l6-122.9c1.4-29.7-9.1-57.9-29.5-79.4-20.5-21.5-48.1-33.4-77.9-33.4-52 0-98 35-111.8 85.1l-85.9 311h-.3v428h472.3c9.2 0 18.2-1.8 26.5-5.4 47.6-20.3 78.3-66.8 78.3-118.4 0-12.6-1.8-25-5.4-37 16.8-22.2 26.1-49.4 26.1-77.7 0-12.6-1.8-25-5.4-37 16.8-22.2 26.1-49.4 26.1-77.7-.2-12.6-2-25.1-5.6-37.1zM112 528v364c0 17.7 14.3 32 32 32h65V496h-65c-17.7 0-32 14.3-32 32z"/>
            </svg>
            <span>{{ post.likes }} 点赞</span>
          </div>
          
          <div class="stat-item">
            <svg class="icon" viewBox="0 0 1024 1024">
              <path d="M573 421c-23.1 0-41 17.9-41 40s17.9 40 41 40c21.1 0 39-17.9 39-40s-17.9-40-39-40zm-280 0c-23.1 0-41 17.9-41 40s17.9 40 41 40c21.1 0 39-17.9 39-40s-17.9-40-39-40z"/>
              <path d="M894 345c-48.1-66-115.3-110.1-189-130v.1c-17.1-19-36.4-36.5-58-52.1-163.7-119-393.5-82.7-513 81-96.3 133-92.2 311.9 6 439l.8 132.6c0 3.2.5 6.4 1.5 9.4 5.3 16.9 23.3 26.2 40.1 20.9L309 806c33.5 11.9 68.1 18.7 102.5 20.6l-.5.4c89.1 64.9 205.9 84.4 313 49l127.1 41.4c3.2 1 6.5 1.6 9.9 1.6 17.7 0 32-14.3 32-32V753c88.1-119.6 90.4-284.9 1-408zM323 735l-12-5-99 31-1-104-8-9c-84.6-103.2-90.2-251.9-11-361 96.4-132.2 281.2-161.4 413-66 132.2 96.1 161.5 280.6 66 412-80.1 109.9-223.5 150.5-348 102z"/>
            </svg>
            <span>{{ post.comments_count }} 评论</span>
          </div>
        </div>
        
        <!-- 评论区 -->
        <div class="comments-section">
          <div class="comments-title">评论 ({{ post.comments.length }})</div>
          
          <div v-if="post.comments.length === 0" class="no-comments">
            暂无评论，快来抢沙发吧~
          </div>
          
          <div v-else class="comments-list">
            <div 
              v-for="comment in post.comments" 
              :key="comment.id"
              class="comment-item"
            >
              <img :src="comment.author.avatar" :alt="comment.author.nickname" class="comment-avatar" />
              <div class="comment-content">
                <div class="comment-author">{{ comment.author.nickname }}</div>
                <div class="comment-text">{{ comment.content }}</div>
                <div class="comment-time">{{ formatTime(comment.created_at) }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { postsAPI } from '../api'

const route = useRoute()
const router = useRouter()

const post = ref(null)
const loading = ref(false)

const fetchPostDetail = async () => {
  loading.value = true
  try {
    const data = await postsAPI.getDetail(route.params.id)
    post.value = data
  } catch (error) {
    console.error('获取帖子详情失败:', error)
  } finally {
    loading.value = false
  }
}

const goBack = () => {
  router.back()
}

const goToUser = () => {
  if (post.value?.author) {
    router.push(`/user/${post.value.author.id}`)
  }
}

const viewImage = (index) => {
  // 图片查看功能，可以后续扩展为图片预览组件
  console.log('查看图片:', index)
}

const formatTime = (time) => {
  const date = new Date(time)
  const now = new Date()
  const diff = now - date
  const seconds = Math.floor(diff / 1000)
  const minutes = Math.floor(seconds / 60)
  const hours = Math.floor(minutes / 60)
  const days = Math.floor(hours / 24)
  
  if (days > 7) {
    return `${date.getFullYear()}-${(date.getMonth() + 1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')}`
  } else if (days > 0) {
    return `${days}天前`
  } else if (hours > 0) {
    return `${hours}小时前`
  } else if (minutes > 0) {
    return `${minutes}分钟前`
  } else {
    return '刚刚'
  }
}

onMounted(() => {
  fetchPostDetail()
})
</script>

<style scoped>
.post-detail-container {
  min-height: 100vh;
  background: #f5f5f5;
  padding: 20px;
}

.detail-wrapper {
  max-width: 800px;
  margin: 0 auto;
}

.back-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background: white;
  border-radius: 20px;
  cursor: pointer;
  margin-bottom: 16px;
  font-size: 14px;
  color: #666;
  transition: all 0.3s;
}

.back-btn:hover {
  background: #ff2442;
  color: white;
}

.back-btn .icon {
  width: 16px;
  height: 16px;
  fill: currentColor;
}

.post-content {
  background: white;
  border-radius: 12px;
  padding: 24px;
}

.post-header {
  margin-bottom: 20px;
}

.author-info {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
}

.author-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  object-fit: cover;
}

.author-meta {
  flex: 1;
}

.author-name {
  font-size: 16px;
  font-weight: 600;
  color: #333;
  margin-bottom: 4px;
}

.author-bio {
  font-size: 13px;
  color: #999;
  margin-bottom: 4px;
}

.post-time {
  font-size: 12px;
  color: #999;
}

.post-title {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  margin-bottom: 16px;
  line-height: 1.4;
}

.post-body {
  font-size: 16px;
  color: #333;
  line-height: 1.8;
  margin-bottom: 20px;
  white-space: pre-wrap;
}

.media-section {
  margin: 20px 0;
}

.image-wrapper {
  margin-bottom: 12px;
  cursor: pointer;
  border-radius: 8px;
  overflow: hidden;
}

.post-image {
  width: 100%;
  height: auto;
  display: block;
  transition: transform 0.3s;
}

.image-wrapper:hover .post-image {
  transform: scale(1.02);
}

.post-video {
  width: 100%;
  border-radius: 8px;
}

.post-stats {
  display: flex;
  gap: 24px;
  padding: 16px 0;
  border-top: 1px solid #f0f0f0;
  border-bottom: 1px solid #f0f0f0;
  margin: 20px 0;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #666;
  font-size: 14px;
}

.stat-item .icon {
  width: 20px;
  height: 20px;
  fill: currentColor;
}

.comments-section {
  margin-top: 24px;
}

.comments-title {
  font-size: 18px;
  font-weight: 600;
  color: #333;
  margin-bottom: 16px;
}

.no-comments {
  text-align: center;
  padding: 40px;
  color: #999;
  font-size: 14px;
}

.comments-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.comment-item {
  display: flex;
  gap: 12px;
}

.comment-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  object-fit: cover;
  flex-shrink: 0;
}

.comment-content {
  flex: 1;
  background: #f8f8f8;
  padding: 12px;
  border-radius: 8px;
}

.comment-author {
  font-size: 14px;
  font-weight: 500;
  color: #333;
  margin-bottom: 6px;
}

.comment-text {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  margin-bottom: 6px;
}

.comment-time {
  font-size: 12px;
  color: #999;
}

.loading {
  text-align: center;
  padding: 40px;
  color: #999;
  font-size: 14px;
}

@media (max-width: 768px) {
  .post-detail-container {
    padding: 12px;
  }
  
  .post-content {
    padding: 16px;
  }
  
  .post-title {
    font-size: 20px;
  }
  
  .post-body {
    font-size: 15px;
  }
}
</style>


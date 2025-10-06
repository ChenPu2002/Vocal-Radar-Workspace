<template>
  <div class="post-card" @click="goToDetail">
    <div class="card-header">
      <div class="author-info" @click.stop="goToUser">
        <img :src="post.author.avatar" :alt="post.author.nickname" class="author-avatar" />
        <div class="author-meta">
          <div class="author-name">{{ post.author.nickname }}</div>
          <div class="post-time">{{ formatTime(post.created_at) }}</div>
        </div>
      </div>
    </div>
    
    <div class="card-content">
      <h3 class="post-title">{{ post.title }}</h3>
      <p class="post-summary">{{ post.content }}</p>
      
      <!-- 图片展示 -->
      <div v-if="post.media_type === 'image' && post.media_urls.length > 0" class="media-container">
        <div :class="['image-grid', `grid-${Math.min(post.media_urls.length, 4)}`]">
          <div 
            v-for="(url, index) in post.media_urls.slice(0, 4)" 
            :key="index"
            class="image-item"
          >
            <img :src="url" :alt="`图片${index + 1}`" class="post-image" />
            <div v-if="index === 3 && post.media_urls.length > 4" class="more-images">
              +{{ post.media_urls.length - 4 }}
            </div>
          </div>
        </div>
      </div>
      
      <!-- 视频展示 -->
      <div v-if="post.media_type === 'video' && post.media_urls.length > 0" class="media-container">
        <div class="video-wrapper">
          <video :src="post.media_urls[0]" class="post-video" controls></video>
        </div>
      </div>
    </div>
    
    <div class="card-footer">
      <div class="action-item">
        <svg class="icon" viewBox="0 0 1024 1024">
          <path d="M885.9 533.7c16.8-22.2 26.1-49.4 26.1-77.7 0-44.9-25.1-87.4-65.5-111.1a67.67 67.67 0 0 0-34.3-9.3H572.4l6-122.9c1.4-29.7-9.1-57.9-29.5-79.4-20.5-21.5-48.1-33.4-77.9-33.4-52 0-98 35-111.8 85.1l-85.9 311h-.3v428h472.3c9.2 0 18.2-1.8 26.5-5.4 47.6-20.3 78.3-66.8 78.3-118.4 0-12.6-1.8-25-5.4-37 16.8-22.2 26.1-49.4 26.1-77.7 0-12.6-1.8-25-5.4-37 16.8-22.2 26.1-49.4 26.1-77.7-.2-12.6-2-25.1-5.6-37.1zM112 528v364c0 17.7 14.3 32 32 32h65V496h-65c-17.7 0-32 14.3-32 32z"/>
        </svg>
        <span>{{ formatNumber(post.likes) }}</span>
      </div>
      
      <div class="action-item">
        <svg class="icon" viewBox="0 0 1024 1024">
          <path d="M573 421c-23.1 0-41 17.9-41 40s17.9 40 41 40c21.1 0 39-17.9 39-40s-17.9-40-39-40zm-280 0c-23.1 0-41 17.9-41 40s17.9 40 41 40c21.1 0 39-17.9 39-40s-17.9-40-39-40z"/>
          <path d="M894 345c-48.1-66-115.3-110.1-189-130v.1c-17.1-19-36.4-36.5-58-52.1-163.7-119-393.5-82.7-513 81-96.3 133-92.2 311.9 6 439l.8 132.6c0 3.2.5 6.4 1.5 9.4 5.3 16.9 23.3 26.2 40.1 20.9L309 806c33.5 11.9 68.1 18.7 102.5 20.6l-.5.4c89.1 64.9 205.9 84.4 313 49l127.1 41.4c3.2 1 6.5 1.6 9.9 1.6 17.7 0 32-14.3 32-32V753c88.1-119.6 90.4-284.9 1-408zM323 735l-12-5-99 31-1-104-8-9c-84.6-103.2-90.2-251.9-11-361 96.4-132.2 281.2-161.4 413-66 132.2 96.1 161.5 280.6 66 412-80.1 109.9-223.5 150.5-348 102z"/>
        </svg>
        <span>{{ formatNumber(post.comments_count) }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const props = defineProps({
  post: {
    type: Object,
    required: true
  }
})

const router = useRouter()

const goToDetail = () => {
  router.push(`/post/${props.post.id}`)
}

const goToUser = () => {
  router.push(`/user/${props.post.author.id}`)
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
    return `${date.getMonth() + 1}-${date.getDate()}`
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

const formatNumber = (num) => {
  if (num >= 10000) {
    return (num / 10000).toFixed(1) + 'w'
  } else if (num >= 1000) {
    return (num / 1000).toFixed(1) + 'k'
  }
  return num.toString()
}
</script>

<style scoped>
.post-card {
  background: white;
  border-radius: 12px;
  padding: 16px;
  cursor: pointer;
  transition: all 0.3s;
  margin-bottom: 12px;
}

.post-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

.card-header {
  margin-bottom: 12px;
}

.author-info {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}

.author-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
}

.author-meta {
  flex: 1;
}

.author-name {
  font-size: 14px;
  font-weight: 500;
  color: #333;
}

.post-time {
  font-size: 12px;
  color: #999;
  margin-top: 2px;
}

.card-content {
  margin-bottom: 12px;
}

.post-title {
  font-size: 16px;
  font-weight: 600;
  color: #333;
  margin-bottom: 8px;
  line-height: 1.4;
}

.post-summary {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-bottom: 12px;
}

.media-container {
  margin-top: 12px;
}

.image-grid {
  display: grid;
  gap: 4px;
  border-radius: 8px;
  overflow: hidden;
}

.grid-1 {
  grid-template-columns: 1fr;
}

.grid-2 {
  grid-template-columns: repeat(2, 1fr);
}

.grid-3 {
  grid-template-columns: repeat(3, 1fr);
}

.grid-4 {
  grid-template-columns: repeat(2, 1fr);
}

.image-item {
  position: relative;
  padding-bottom: 100%;
  overflow: hidden;
  background: #f5f5f5;
}

.post-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.more-images {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  font-weight: bold;
}

.video-wrapper {
  position: relative;
  padding-bottom: 56.25%;
  background: #000;
  border-radius: 8px;
  overflow: hidden;
}

.post-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.card-footer {
  display: flex;
  align-items: center;
  gap: 20px;
  padding-top: 12px;
  border-top: 1px solid #f0f0f0;
}

.action-item {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #999;
  font-size: 13px;
  cursor: pointer;
  transition: color 0.3s;
}

.action-item:hover {
  color: #ff2442;
}

.icon {
  width: 18px;
  height: 18px;
  fill: currentColor;
}

@media (max-width: 768px) {
  .post-card {
    padding: 12px;
    border-radius: 8px;
  }
  
  .author-avatar {
    width: 36px;
    height: 36px;
  }
  
  .post-title {
    font-size: 15px;
  }
  
  .post-summary {
    font-size: 13px;
  }
}
</style>


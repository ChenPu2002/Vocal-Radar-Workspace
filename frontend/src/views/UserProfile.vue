<template>
  <div class="user-profile-container">
    <div v-if="loading && !user" class="loading">加载中...</div>
    
    <div v-else-if="user" class="profile-wrapper">
      <div class="back-btn" @click="goBack">
        <svg class="icon" viewBox="0 0 1024 1024">
          <path d="M724 218.3V141c0-6.7-7.7-10.4-12.9-6.3L260.3 486.8a31.86 31.86 0 0 0 0 50.3l450.8 352.1c5.3 4.1 12.9.4 12.9-6.3v-77.3c0-4.9-2.3-9.6-6.1-12.6l-360-281 360-281.1c3.8-3 6.1-7.7 6.1-12.6z"/>
        </svg>
        返回
      </div>
      
      <div class="user-card">
        <div class="user-info">
          <img :src="user.avatar" :alt="user.nickname" class="user-avatar" />
          <div class="user-meta">
            <h1 class="user-name">{{ user.nickname }}</h1>
            <p class="user-bio">{{ user.bio }}</p>
            <div class="user-stats">
              <div class="stat-item">
                <span class="stat-value">{{ user.post_count }}</span>
                <span class="stat-label">帖子</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="user-posts-section">
        <div class="section-title">TA的帖子</div>
        
        <div v-if="loadingPosts && posts.length === 0" class="loading">加载中</div>
        
        <div v-else class="posts-list">
          <PostCard 
            v-for="post in posts" 
            :key="post.id" 
            :post="post" 
          />
          
          <div v-if="loadingPosts" class="loading">加载更多中</div>
          <div v-if="!hasMore && posts.length > 0" class="no-more">没有更多了</div>
          <div v-if="posts.length === 0" class="no-posts">暂无帖子</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import PostCard from '../components/PostCard.vue'
import { usersAPI } from '../api'

const route = useRoute()
const router = useRouter()

const user = ref(null)
const posts = ref([])
const loading = ref(false)
const loadingPosts = ref(false)
const currentPage = ref(1)
const hasMore = ref(true)
const pageSize = 10

const fetchUserDetail = async () => {
  loading.value = true
  try {
    const data = await usersAPI.getDetail(route.params.id)
    user.value = data
  } catch (error) {
    console.error('获取用户详情失败:', error)
  } finally {
    loading.value = false
  }
}

const fetchUserPosts = async (page = 1) => {
  if (loadingPosts.value) return
  
  loadingPosts.value = true
  try {
    const response = await usersAPI.getPosts(route.params.id, {
      page,
      page_size: pageSize
    })
    
    if (page === 1) {
      posts.value = response.data
    } else {
      posts.value = [...posts.value, ...response.data]
    }
    
    hasMore.value = posts.value.length < response.total
    currentPage.value = page
  } catch (error) {
    console.error('获取用户帖子失败:', error)
  } finally {
    loadingPosts.value = false
  }
}

const handleScroll = () => {
  const scrollTop = window.pageYOffset || document.documentElement.scrollTop
  const windowHeight = window.innerHeight
  const documentHeight = document.documentElement.scrollHeight
  
  if (scrollTop + windowHeight >= documentHeight - 200) {
    if (!loadingPosts.value && hasMore.value) {
      fetchUserPosts(currentPage.value + 1)
    }
  }
}

const goBack = () => {
  router.back()
}

onMounted(() => {
  fetchUserDetail()
  fetchUserPosts(1)
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.user-profile-container {
  min-height: 100vh;
  background: #f5f5f5;
  padding: 20px;
}

.profile-wrapper {
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

.user-card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  margin-bottom: 20px;
}

.user-info {
  display: flex;
  gap: 20px;
  align-items: flex-start;
}

.user-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  flex-shrink: 0;
}

.user-meta {
  flex: 1;
}

.user-name {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  margin-bottom: 8px;
}

.user-bio {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
  margin-bottom: 16px;
}

.user-stats {
  display: flex;
  gap: 24px;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.stat-value {
  font-size: 20px;
  font-weight: bold;
  color: #ff2442;
}

.stat-label {
  font-size: 13px;
  color: #999;
}

.user-posts-section {
  background: white;
  border-radius: 12px;
  padding: 20px;
}

.section-title {
  font-size: 18px;
  font-weight: 600;
  color: #333;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 2px solid #ff2442;
}

.posts-list {
  display: flex;
  flex-direction: column;
}

.loading {
  text-align: center;
  padding: 20px;
  color: #999;
  font-size: 14px;
}

.no-more {
  text-align: center;
  padding: 30px;
  color: #ccc;
  font-size: 14px;
}

.no-posts {
  text-align: center;
  padding: 40px;
  color: #999;
  font-size: 14px;
}

@media (max-width: 768px) {
  .user-profile-container {
    padding: 12px;
  }
  
  .user-card {
    padding: 16px;
  }
  
  .user-info {
    gap: 12px;
  }
  
  .user-avatar {
    width: 60px;
    height: 60px;
  }
  
  .user-name {
    font-size: 20px;
  }
  
  .user-posts-section {
    padding: 16px;
  }
}
</style>


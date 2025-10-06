<template>
  <div class="home-container">
    <div class="content-wrapper">
      <div v-if="loading && posts.length === 0" class="loading">加载中</div>
      
      <div v-else class="posts-list">
        <PostCard 
          v-for="post in posts" 
          :key="post.id" 
          :post="post" 
        />
        
        <div v-if="loading" class="loading">加载更多中</div>
        <div v-if="!hasMore && posts.length > 0" class="no-more">没有更多了</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import PostCard from '../components/PostCard.vue'
import { postsAPI } from '../api'

const posts = ref([])
const loading = ref(false)
const currentPage = ref(1)
const hasMore = ref(true)
const pageSize = 10

const fetchPosts = async (page = 1) => {
  if (loading.value) return
  
  loading.value = true
  try {
    const response = await postsAPI.getList({
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
    console.error('获取帖子列表失败:', error)
  } finally {
    loading.value = false
  }
}

const handleScroll = () => {
  const scrollTop = window.pageYOffset || document.documentElement.scrollTop
  const windowHeight = window.innerHeight
  const documentHeight = document.documentElement.scrollHeight
  
  if (scrollTop + windowHeight >= documentHeight - 200) {
    if (!loading.value && hasMore.value) {
      fetchPosts(currentPage.value + 1)
    }
  }
}

onMounted(() => {
  fetchPosts(1)
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.home-container {
  min-height: 100vh;
  background: #f5f5f5;
}

.content-wrapper {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
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

@media (max-width: 768px) {
  .content-wrapper {
    padding: 12px;
  }
}
</style>


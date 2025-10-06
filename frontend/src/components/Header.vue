<template>
  <header class="header">
    <div class="header-content">
      <div class="logo-section" @click="handleRefresh">
        <div class="radar-icon">
          <svg viewBox="0 0 100 100" class="radar-svg">
            <circle cx="50" cy="50" r="45" class="radar-circle" />
            <circle cx="50" cy="50" r="30" class="radar-circle" />
            <circle cx="50" cy="50" r="15" class="radar-circle" />
            <line x1="50" y1="50" x2="50" y2="5" class="radar-line" />
            <circle cx="50" cy="50" r="5" class="radar-dot" />
          </svg>
        </div>
        <h1 class="logo-text">原声雷达</h1>
      </div>
      
      <div class="user-section" v-if="userStore.currentUser">
        <router-link :to="`/user/${userStore.currentUser.id}`" class="user-link">
          <img :src="userStore.currentUser.avatar" :alt="userStore.currentUser.nickname" class="user-avatar" />
          <span class="user-name">{{ userStore.currentUser.nickname }}</span>
        </router-link>
      </div>
    </div>
  </header>
</template>

<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '../stores/user'

const emit = defineEmits(['refresh'])
const userStore = useUserStore()

onMounted(() => {
  userStore.init()
})

const handleRefresh = () => {
  emit('refresh')
}
</script>

<style scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  z-index: 1000;
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  height: 100%;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  user-select: none;
}

.radar-icon {
  width: 36px;
  height: 36px;
  position: relative;
}

.radar-svg {
  width: 100%;
  height: 100%;
  animation: radar-spin 3s linear infinite;
}

.radar-circle {
  fill: none;
  stroke: #ff2442;
  stroke-width: 1.5;
  opacity: 0.6;
}

.radar-line {
  stroke: #ff2442;
  stroke-width: 2;
  transform-origin: 50% 50%;
}

.radar-dot {
  fill: #ff2442;
}

@keyframes radar-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.logo-text {
  font-size: 24px;
  font-weight: bold;
  color: #333;
  letter-spacing: 1px;
}

.user-section {
  display: flex;
  align-items: center;
}

.user-link {
  display: flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  color: #333;
  padding: 6px 12px;
  border-radius: 20px;
  transition: background 0.3s;
}

.user-link:hover {
  background: #f5f5f5;
}

.user-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  object-fit: cover;
}

.user-name {
  font-size: 14px;
  font-weight: 500;
}

@media (max-width: 768px) {
  .header {
    height: 50px;
  }
  
  .header-content {
    padding: 0 15px;
  }
  
  .radar-icon {
    width: 28px;
    height: 28px;
  }
  
  .logo-text {
    font-size: 18px;
  }
  
  .user-name {
    display: none;
  }
  
  .user-avatar {
    width: 28px;
    height: 28px;
  }
}
</style>


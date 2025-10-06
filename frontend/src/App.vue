<template>
  <div id="app" class="app-container">
    <Header @refresh="handleRefresh" />
    <main class="main-content">
      <router-view :key="refreshKey" />
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import Header from './components/Header.vue'

const router = useRouter()
const refreshKey = ref(0)

const handleRefresh = () => {
  // 刷新当前页面
  if (router.currentRoute.value.path === '/') {
    refreshKey.value++
  } else {
    router.push('/')
  }
}
</script>

<style scoped>
.app-container {
  min-height: 100vh;
  background: #f5f5f5;
}

.main-content {
  padding-top: 60px;
  min-height: calc(100vh - 60px);
}

@media (max-width: 768px) {
  .main-content {
    padding-top: 50px;
  }
}
</style>


import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const currentUser = ref(null)
  const loading = ref(false)

  // 获取随机模拟用户
  const fetchRandomUser = async () => {
    if (currentUser.value) return
    
    loading.value = true
    try {
      const response = await axios.get('/api/random-user')
      currentUser.value = response.data
      localStorage.setItem('currentUser', JSON.stringify(response.data))
    } catch (error) {
      console.error('获取用户失败:', error)
    } finally {
      loading.value = false
    }
  }

  // 从本地存储恢复用户
  const restoreUser = () => {
    const stored = localStorage.getItem('currentUser')
    if (stored) {
      currentUser.value = JSON.parse(stored)
    }
  }

  // 初始化：尝试从本地存储恢复，否则获取随机用户
  const init = async () => {
    restoreUser()
    if (!currentUser.value) {
      await fetchRandomUser()
    }
  }

  return {
    currentUser,
    loading,
    fetchRandomUser,
    init,
  }
})


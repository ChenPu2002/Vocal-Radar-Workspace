import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  timeout: 10000,
})

// 请求拦截器
api.interceptors.request.use(
  (config) => {
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// 响应拦截器
api.interceptors.response.use(
  (response) => {
    return response.data
  },
  (error) => {
    console.error('API错误:', error)
    return Promise.reject(error)
  }
)

// API方法
export const postsAPI = {
  // 获取帖子列表
  getList(params) {
    return api.get('/posts', { params })
  },
  
  // 获取帖子详情
  getDetail(id) {
    return api.get(`/posts/${id}`)
  },
}

export const usersAPI = {
  // 获取用户详情
  getDetail(id) {
    return api.get(`/users/${id}`)
  },
  
  // 获取用户的帖子
  getPosts(id, params) {
    return api.get(`/users/${id}/posts`, { params })
  },
  
  // 获取随机用户
  getRandom() {
    return api.get('/random-user')
  },
}

export const commentsAPI = {
  // 获取评论列表
  getList(postId) {
    return api.get('/comments', { params: { post_id: postId } })
  },
}

export default api


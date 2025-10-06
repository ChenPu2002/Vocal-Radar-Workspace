import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import PostDetail from '../views/PostDetail.vue'
import UserProfile from '../views/UserProfile.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/post/:id',
    name: 'PostDetail',
    component: PostDetail,
  },
  {
    path: '/user/:id',
    name: 'UserProfile',
    component: UserProfile,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router


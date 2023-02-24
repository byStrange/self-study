import { createRouter, createWebHistory } from 'vue-router'
import Welcome from '../views/Welcome.vue';
import Register from '../views/Register.vue';
import Login from '../views/Login.vue';
import More from '@/views/More.vue'
const routes = [
  {
    path: '/',
    name: "Welcome",
    component: Welcome
  },
  {
    path: '/register',
    name: "Register",
    component: Register
  },
  {
    path: '/login',
    name: "Login",
    component: Login
  }, 
  {
    path: '/more',
    name: "More",
    component: More
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

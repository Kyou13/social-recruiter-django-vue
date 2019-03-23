import Vue from 'vue'
import Router from 'vue-router'
import Top from '@/views/Top'
import Login from '@/views/Login'
import DashBoard from '@/views/DashBoard'

import Store from '@/store/index.js'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Top',
      component: Top
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/dashboard',
      name: 'DashBoard',
      component: DashBoard,
      meta: { requiresAuth: true }
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(page => page.meta.requiresAuth) && !Store.state.isLoggedIn) {
    next('/')
  } else {
    next()
  }
})

export default router

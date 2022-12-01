import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SearchView from '../views/SearchView.vue'
import TestView from '../views/TestView.vue'
import Playground from '../views/Playground.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/test',
    name: 'test',
    component: TestView
  },
  {
    path: '/playground',
    name: 'playground',
    component: Playground,
  }
]

const router = new VueRouter({
  routes
})

export default router

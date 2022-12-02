import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SearchView from '../views/SearchView.vue'
import NewHomeView from '../views/NewHomePage.vue'
import Playground from '../views/Playground.vue'
import PicSearchGalleryView from '../views/PicSearchGallery.vue'
Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/',
  //   name: 'home',
  //   component: HomeView
  // },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/',
    name: 'home',
    component: NewHomeView
  },
  {
    path: '/playground',
    name: 'playground',
    component: Playground,
  },
  {
    path: '/picsearch',
    name: 'picsearch',
    component: PicSearchGalleryView,
  }
]

const router = new VueRouter({
  routes
})

export default router

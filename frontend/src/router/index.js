import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import(/* webpackChunkName: "about" */ '../views/Home.vue')
  },
  {
    path: '/bundesliga',
    name: 'bundesliga',
    component: () => import(/* webpackChunkName: "bundesliga" */ '../views/Bundesliga.vue')
  },
  {
    path: '/laliga',
    name: 'laliga',
    component: () => import(/* webpackChunkName: "laliga" */ '../views/La_liga.vue')
  },
  {
    path: '/ligueone',
    name: 'ligueone',
    component: () => import(/* webpackChunkName: "ligueone" */ '../views/Ligue_one.vue')
  },
  {
    path: '/premierleague',
    name: 'premierleague',
    component: () => import(/* webpackChunkName: "premierleague" */ '../views/Premier_league.vue')
  },
  {
    path: '/seriea',
    name: 'seriea',
    component: () => import(/* webpackChunkName: "seriea" */ '../views/Serie_a.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

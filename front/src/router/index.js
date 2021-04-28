import { createWebHistory, createRouter } from 'vue-router'
import Room from '@/views/Room'
import NotFound from '@/views/NotFound'
import Home from '@/views/Home'
import Signin from '@/views/Signin'
import Signup from '@/views/Signup'
import Profile from '@/views/Profile'
//import Signout from '@/views/Signout'
import store from '@/store'

const authGuard = (to, from, next) => {
    if (store.getters.isAuthenticated) {
      next();
    } else {
      next("/signin")
    }
  };


const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/room/:code',
        name: 'Room',
        component: Room,
        beforeEnter: authGuard
    },
    {
        path: '/:catchAll(.*)',
        name: '404',
        component: NotFound,
    },
    {
        path: '/signup',
        name: 'Signup',
        component: Signup,
    },
    {
        path: '/signin',
        name: 'Signin',
        component: Signin,
    },
    {
        path: '/profile',
        name: 'Profile',
        component: Profile,
        beforeEnter: authGuard
    },
    
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
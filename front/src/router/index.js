import { createWebHistory, createRouter } from 'vue-router'
import Room from '@/views/Room'
import NotFound from '@/views/NotFound'
import Home from '@/views/Home'
import Signin from '@/views/Signin'
import Signup from '@/views/Signup'

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
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
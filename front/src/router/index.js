import { createWebHistory, createRouter } from 'vue-router'
import Room from '@/views/Room'
import NotFound from '@/views/NotFound'
import Home from '@/views/Home'

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
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
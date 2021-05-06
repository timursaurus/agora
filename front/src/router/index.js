import { createWebHistory, createRouter } from 'vue-router'
import Room from '@/views/Room'
import NotFound from '@/views/NotFound'
import Home from '@/views/Home'
import Signin from '@/views/Signin'
import Signup from '@/views/Signup'
import Profile from '@/views/Profile'

const authGuard = (to, from, next) => {
    if (localStorage.getItem('accessToken')) next(); else next('/signin')
    
}


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
        props: true,
        beforeEnter: authGuard
        // beforeEnter: (to, from, next) => {
        //     function isValid (param) {
        //         console.log(param)
        //     }
          
        //     if (!isValid(to.params.code)) {
        //         next({ name: '404' });
        //     }
          
        //     else next();
        // }
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
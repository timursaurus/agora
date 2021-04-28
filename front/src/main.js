import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
// import '@/assets/styles/app.css'
import './assets/styles/app.css'


createApp(App).use(store).use(router).mount('#app')

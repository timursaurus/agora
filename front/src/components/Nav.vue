<template>
    <nav class='bg-nicegray' >
        <div class="container mx-auto px-16">
            <div class="grid grid-cols-12 py-2 ">
                <div class='col-span-3 block w-40 flex items-center '>
                    <router-link to='/' >
                        <h1 class='text-white text-3xl'>Agora</h1>
                    </router-link>
                </div>
                <div class='col-span-6 block' >
                    <div class="relative">
                        <div class='absolute top-0 right-0 h-12 w-12 flex justify-center items-center ' >
                            <svg class="h-6 z-30 hover:text-gray-200 cursor-pointer w-6 text-gray-400"  xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd" /></svg>
                        </div>
                        <input 
                        @focus='searchmode = !searchmode'
                        @blur='searchmode = !searchmode; Defaults()'
                        @input='Search'
                        @change='Search'
                        v-model='search'
                        class='z-20 relative w-full text-gray-200 bg-nicegray-light pr-8 rounded-md h-12 px-4 focus:outline-none text-lg placeholder-gray-400' placeholder='Search' type="text">
                        <transition name='fade' mode="out-in" >
                            <div v-show='searchmode' class=' z-10 w-full my-1 rounded-md text-gray-200 text-lg bg-nicegray-light absolute bg-opacity-50 backdrop-filter backdrop-blur filter drop-shadow ' >
                                <ul v-for='hint in hints' :key=hint >
                                    <li class='py-1 rounded-md cursor-pointer duration-200 px-4 hover:text-nicegray-dark hover:bg-gray-400' >
                                        {{ hint }} 
                                    </li>
                                </ul>
                                <ul v-for='room in rooms' :key=room >
                                    <li class='py-1 flex items-center justify-between rounded-md cursor-pointer duration-200 px-4 hover:text-nicegray-dark hover:bg-gray-400' >
                                        <p>{{room.title }}</p> 
                                        <p class='text-sm right-0'>
                                            <svg xmlns="http://www.w3.org/2000/svg" class="opacity-50 hover:opacity-100 pl-2 h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
                                         </p>
                                    </li>
                                </ul>
                                <ul v-for='user in users' :key=user >
                                    <li class='py-1 flex items-center justify-between rounded-md cursor-pointer duration-200 px-4 hover:text-nicegray-dark hover:bg-gray-400' > 
                                        <p>@{{user.username }}</p>
                                         <p class='text-sm right-0'>
                                            <svg xmlns="http://www.w3.org/2000/svg" class="opacity-50 hover:opacity-100 pl-2 h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
                                         </p>
                                    </li>
                                </ul>
                                <ul v-for='category in categories' :key=category >
                                    <li class='py-1 flex items-center justify-between rounded-md cursor-pointer duration-200 px-4 hover:text-nicegray-dark hover:bg-gray-400' > 
                                        <p>#{{category.name }}</p>
                                        <p class='text-sm right-0'>
                                            <svg xmlns="http://www.w3.org/2000/svg" class="opacity-50 hover:opacity-100 pl-2 h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
                                         </p>
                                    </li>
                                </ul>

                            </div>
                        </transition>
                    </div>
                </div>
                <div class='col-span-3 flex justify-end items-center' >
                    <router-link to='/signin' >
                        <!-- <h1  class='text-white text-2xl' >Login</h1> -->
                        <div class='text-gray-400 text-lg bg-nicegray-light flex justify-center items-center px-6 h-12 max-w-full rounded-full hover:text-nicegray-dark hover:bg-gray-400' v-if='!isAuthenticated' >
                            <button>Sign in</button>
                        </div>
                    </router-link>
                    <span v-if="isAuthenticated">           
                        <a class='text-white' href="#" @click.prevent="SignOut">Sign out</a>
                    </span>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
import store from "@/store";
import HTTP from '@/api'
export default {
    name: 'Nav',
    data() {
        return {
            search: '',
            searchmode: false,
            hints: ['@user', '#category'],
            rooms: [],
            users: [],
            categories: []
        }
    },
    setup() {
        return {
            SignOut: () => store.dispatch('SignOut')
        }
    },
    computed: {
        isAuthenticated(){
            return this.$store.getters.isAuthenticated
        }
    },
    methods: {
        Search() {
            if (this.search[0] == '@'){
                if (this.search.length > 1) {
                    HTTP.get('/api/user/?search=' + this.search.slice(1))
                    .then((res) => {
                        this.hints = []
                        this.users = res.data 
                    })
                } else {
                    this.users = []
                }
            }
            else if (this.search[0] == '#'){
                if (this.search.length > 1) {
                    HTTP.get('/api/category/?search=' + this.search.slice(1))
                    .then((res) => {
                        this.hints = []
                        this.categories = res.data
                    })
                } else {
                    this.categories = []
                }
            }
            else if (this.search.length >= 1) {
                HTTP.get('/api/room/?search=' + this.search)
                .then((res) => {
                    this.hints = []
                    this.rooms = res.data
                })
                
            }
            else if (this.search.length < 1) {
                this.Defaults()
            }
            
        },
        Defaults(){
            setTimeout(() => {
                this.hints = ['@user', '#category']
                this.rooms = []
                this.users = []
                this.categories = []
            }, 300)
            
        }
    },
    mounted() {
        this.Defaults()
    }
    
    
}

</script>

<style scoped>

.fade-enter-from {
    opacity: 0;
    transform: translateY(-60px);
    transform: scale(0.9)
}
.fade-enter-to {
    opacity: 1;
    transform: translateY(0px);
    transform: scale(1)
}
.fade-enter-active {
    transition: all 0.2s ease-out; 
}
.fade-leave-from {
    opacity: 1;
    transform: translateY(0px);
}
.fade-leave-to {
    opacity: 0;
    transform: translateY(-60px);
    /* transform: scale(0.9) */
}
.fade-leave-active {
    transition: all 0.2s ease-out;
}




</style>
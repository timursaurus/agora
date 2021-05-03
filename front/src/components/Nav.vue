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
                        @change='Search'
                        v-model='search'
                        class='z-20 relative w-full text-gray-200 bg-nicegray-light pr-8 rounded-md h-12 px-4 focus:outline-none text-lg placeholder-gray-400' placeholder='Search' type="text">
                        <transition name='fade' mode="out-in" >
                            <div v-show='searchmode' class=' z-10 w-full my-1 py-1 rounded-md text-gray-200 text-lg bg-nicegray-light absolute bg-opacity-50 backdrop-filter backdrop-blur filter drop-shadow ' >
                                <ul>
                                    <li v-for='suggestion in suggestions' :key=suggestion class='py-1 rounded-md cursor-pointer duration-200 px-4 hover:text-nicegray-dark hover:bg-gray-400' > {{ suggestion }} </li>
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

export default {
    name: 'Nav',
    data() {
        return {
            search: '',
            suggestions: [],
            searchmode: false
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
                console.log('Searching for users')
                this.suggestions = []
            }
            else if (this.search[0] == '#'){
                console.log('Searching for categories')
                this.suggestions = []
            }
            else {
                console.log('Regular search')
            }
            
        },
        Defaults(){
            this.suggestions = ['@user search', '#category search']
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
}
.fade-enter-to {
    opacity: 1;
    transform: translateY(0px);
}
.fade-enter-active {
    transition: all 0.2s ease-out; 
}
.fade-leave-from {
    opacity: 1;
}
.fade-leave-to {
    opacity: 0;
    transform: translateY(-60px);
}
.fade-leave-active {
    transition: all 0.2s ease-out;
}


</style>
<template>
    <div class='container'>
        <div class='bg-nicegray h-20 px-16' >
            <div class="flex pt-4 " >
                <transition-group class='categories mt-2 container mx-auto overflow-x-auto flex flex-row items-center ' name='chips' tag='div'>
                    <router-link :to="{ name: 'CreateRoom', }" >
                        <button class='text-gray-200 bg-green-600 max-w-full whitespace-nowrap  rounded-full hover:text-nicegray-dark hover:bg-green-400 h-8 px-6 mx-1 cursor-pointer duration-200' >Create Room</button>
                    </router-link>
                    <button v-for='category in categories' :key=category.name
                    class='text-gray-400 bg-nicegray-light max-w-full whitespace-nowrap  rounded-full hover:text-nicegray-dark hover:bg-gray-400 h-8 px-6 mx-1 cursor-pointer duration-200'
                    >
                        {{ category.name  }}
                    </button>
                </transition-group>
                <div class='absolute mx-10 left-0 w-12 h-12 bg-nicegray filter blur-sm ' ></div>
                <div class='absolute mx-10 right-0 w-12 h-12 bg-nicegray filter blur-sm '></div>
            </div>
        </div>
    </div>
</template>

<script>
import HTTP from '@/api'
export default {
    name: 'Filters',
    data() {
        return {
            categories: [],

        }
    },
    components: {
    },
    methods: {
        getCategories() {
            HTTP.get('api/category/')
            .then((res) => {
                this.categories = res.data
            })
        },
        scrollLeft() {

        }
    },
    mounted() {
        this.getCategories()
    }
}
</script>

<style scoped>

.categories::-webkit-scrollbar { 
    width: 0;
    height: 0;
}

.chips-enter-from {
    opacity: 0;
    transform: translateX(100px)
}
.chips-enter-to {
    opacity: 1;
    transform: translateX(0)
}
.chips-enter-active {
    transition: all .5s ease;
}


</style>
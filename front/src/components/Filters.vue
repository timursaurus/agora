<template>
    <div class='container'>
        <div class='bg-nicegray h-20 px-16' >
            <div class="flex pt-4 " >
                <div class='absolute mx-10 left-0 w-12 h-12 bg-nicegray filter blur-sm ' ></div>
                <div class='categories mt-2 container mx-auto overflow-x-auto flex flex-row items-center ' >
                    <button v-for='category in categories' :key=category.name
                    class='text-gray-400 bg-nicegray-light max-w-full whitespace-nowrap  rounded-full hover:text-nicegray-dark hover:bg-gray-400 h-8 px-6 mx-1 cursor-pointer duration-200'
                    >
                        {{ category.name  }}
                    </button>
                </div>
                <div class='absolute mx-10 right-0 w-12 h-12 bg-nicegray filter blur-sm  '></div>
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

</style>
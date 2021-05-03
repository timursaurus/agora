<template>
    <div class='container'>
        <div class='bg-nicegray h-20 px-16' >
            <div class="flex">
                <div class='mt-3 text-gray-400 bg-nicegray-light rounded-md'>
                    Filters - WIP
                </div>
                <div class='categories container mx-auto overflow-x-auto flex flex-row items-center ' >
                    <button v-for='category in categories' :key=category.name
                    class='text-gray-400 bg-nicegray-light max-w-full whitespace-nowrap  rounded-full hover:text-nicegray-dark hover:bg-gray-400 h-8 px-6 mx-1 cursor-pointer duration-200'
                    >
                        {{ category.name  }}
                    </button>
                </div>
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
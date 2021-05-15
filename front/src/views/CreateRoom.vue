<template>
    <div class='bg-black' >
        <form @submit.prevent='goLive' class='mt-20' >
            <input placeholder='Room title' v-model='form.title' >
            <textarea placeholder='Room description' v-model='form.description'></textarea>
            <select   v-model='form.category' 
                class='z-10 my-1 rounded-md text-gray-200 text-lg bg-nicegray-light absolute bg-opacity-50 backdrop-filter backdrop-blur filter drop-shadow ' 
            >
                <option v-for='category in options.categories' :key='category' :value='category.id' 
                    class='py-1 rounded-md cursor-pointer duration-200 px-4 hover:text-nicegray-dark hover:bg-gray-400'
                >
                    {{ category.name }}
                </option>
            </select>
            <input placeholder='Room code' v-model='form.code' >
            <div>
                <button class='bg-indigo-700 text-white' type='submit' >Go live</button>
            </div>
        </form>
    </div>
</template>

<script>
import HTTP from '@/api'
export default {
    data() {
        return {
            form: {
                code: null,
                title: '',
                description: '',
                privacy: 'public',
                category: null,
                host: null,
            },
            options: {
                categories: []
            }
        }
    },
    methods: {
        getCats() {
            HTTP.get('api/category/')
            .then((res) => {
                this.options.categories = res.data
            })
        },
        goLive() {
            let data = this.form
            HTTP.post('api/room/create', data)
            
        },

    },
    mounted() {
        this.getCats()
    }
}
</script>

<style>

</style>
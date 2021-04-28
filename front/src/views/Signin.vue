<template>
    <div class='min-h-screen' >
        <Nav />
        <div>
            <form @submit.prevent='onSubmit()' class='bg-white py-8 px-6 shadow rounded-lg'>
                <div>
                    <label for='email' class='block text-gray-700 text-sm font-medium '>Email</label>
                    <div>
                        <input
                        v-model='model.email'
                        class='border border-gray-300 px-3 py-2 rounded-lg shadow-sm focus:outline-none focus:border-indigo-500' 
                        id='email' name='email' required >
                    </div> 
                </div>
                <div>
                    <label for="password" class='block text-gray-700 text-sm font-medium' >Password</label>
                    <div>
                        <input
                        v-model='model.password'
                        class='border border-gray-300 px-3 py-2 rounded-lg shadow-sm focus:outline-none focus:border-indigo-500' 
                        id='password' name='password' required>
                    </div>
                </div>
                <div class='mt-3'>
                    <button class='block bg-red-100' >Sign in</button>
                </div>
            </form>
        </div>
        <Footer />
    </div>
</template>

<script>
import { reactive } from 'vue'
import store from '@/store'
import Nav from '@/components/Nav'
import Footer from '@/components/Footer'

export default {
    name: 'Signin',
    // data() {
    //     return{
    //         form: {
    //             email: '',
    //             password: '',
    //         },
    //         errors: [],
    //         incorrectAuth: false,
    //     }
    // },
    setup() {
        const model = reactive({ username: '', password: ''})
        function onSubmit() {
            store.dispatch('SignIn', model)
            console.log(model)
        }

        return {
            model,
            onSubmit
        }
    },
    components: {
        Nav,
        Footer,

    },


    methods: {
        // Signin() {
        //     let data = this.form
        //     HTTP.post('token/', data).then((res) => {
        //         localStorage.setItem('access_token', res.data.access)
		// 		localStorage.setItem('refresh_token', res.data.refresh)
		// 		HTTP.defaults.headers['Authorization'] = 'JWT ' + localStorage.getItem('access_token')
        //     })
        // }
        // Signin(){
        //     let data = this.form
        //     console.log(data)
        //     HTTP.post('api/token/', data).then((res) => {
        //         console.log(res.data)
        //         this.$store.dispatch('SignIn', res.data)
        //         .then(() => {
        //         this.$router.push({name: 'Home'})
        //             }).catch(err => {
        //             console.log(err)
        //             this.incorrectAuth = true
        //     })
        //     })
            
        // }


        
    }
}
</script>

<style>

</style>
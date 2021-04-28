<template>
    <div>
        <Nav />
        <div class='container'>
            <div class='bg-nicegray h-20 px-16' >
                <div class="flex">
                    <div class='mt-3 text-gray-400 bg-nicegray-light rounded-md'>
                        Filters - WIP
                    </div>
                </div>
            </div>
            <div class="container mx-auto bg-gray-600 min-h-screen px-16 ">
                <h1 class='text-7xl text-white '>
                    <span class='text-transparent bg-gradient-to-r bg-clip-text from-blue-500 to-green-500'>Agora,</span>
                    <br>
                    lol
                </h1>
            </div>
        </div>
        <Footer />
    </div>
</template>

<script>
import Nav from '@/components/Nav'
import Footer from '@/components/Footer'
export default {
    name: 'Home',
    data(){

    },
    components: {
        Nav,
        Footer,
    }
}
</script>

<style>

</style>
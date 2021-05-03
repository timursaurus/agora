<template>
    <div>
        <Nav />
        <Filters />
        <div>
            <h1>bla</h1>
        </div>
        <Footer />
    </div>
</template>

<script>
import Nav from '@/components/Nav'
import Filters from '@/components/Filters'
import Footer from '@/components/Footer'
export default {
    name: 'Home',
    data(){

    },
    components: {
        Nav,
        Filters,
        Footer,
    }
}
</script>

<style>

</style>
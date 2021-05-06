<template>
    <div>
        <div>
            <h1>INSIDE ROOM {{ code }} </h1>
        </div>
    </div>
</template>

<script>
export default {
    props: ['code',],
    data(){
        return {
            // code: this.$route.params.code
        }
    },
    components: {
        
    }
}
</script>

<style>

</style>
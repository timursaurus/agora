<template>
    <div>
        
        
        <div v-for='room in rooms' :key=room.code
        class='bg-black w-64 my-4'
        >   
            <div class='w-full py-4 px-4 ' >
                <p class='text-4xl text-white font-medium '>{{ room.title }}</p>
                <p class='text-white text-lg opacity-50' > #{{room.category}} </p>
                <p class='text-white text-lg opacity-80 ' >Hosted by {{room.host}} </p>
            </div>
            <div>
                
            </div>
            <div class='bg-indigo-700 p-2 text-white text-xl ' >
                <router-link :to="{ name: 'Room', params: { code: room.code} }" class='flex' >
                    <button class='right-0' >Join</button>
                </router-link>
            </div>

            <!-- </router-link> -->
        </div>
    </div>
</template>

<script>
import HTTP from '@/api'
// import router from '@/router'
export default {
    name: 'Rooms',
    data() {
      return {
        rooms: [],
        code: this.$route.params.code
      }
    },
    methods: {
        getRooms() {
            HTTP.get('api/room/')
            .then((res) => {
                console.log(res.data)
                this.rooms = res.data
            })
        },
    },
    mounted() {
        this.getRooms()
    },

}
</script>

<style>
    
</style>
<template>
    <div>
        
        <!-- <ul>
            <li v-for='room in rooms' :key=room  >
                {{ room.title }}
                {{ room.description }}
                {{ room.category_name }}
                {{ room.host_name }}
            </li>
        </ul> -->
        <div v-for='room in rooms' :key=room.code>
            <router-link :to="{ name: 'Room', params: { code: room.code} }" >
                <h1> {{room.title}} </h1>
            </router-link>
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
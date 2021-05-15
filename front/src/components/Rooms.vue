<template>
    <div class='bg-black ' >
        
        <div class='mx-8 grid grid-flow-row grid-cols-4 gap-1' > 
            <div v-for='room in rooms' :key=room.code
            class='w-80 py-8'
            >   
                <div class='w-full bg-white border-t-8 hover:border-0 duration-200 border-indigo-700 py-4 px-4 ' >
                    <div class='flex h- justify-between ' >
                        <p class='text-3xl h-10 truncate hover:overflow-clip text-black font-medium '>{{ room.title }}</p>
                        <router-link :to="{ name: 'Room', params: { code: room.code, title: room.title, description: room.description,   host: room.host_name, category: room.category_name }}" class='hover:text-indigo-700 duration-200' >
                            <svg xmlns="http://www.w3.org/2000/svg" class="text-lg duration-200 hover:w-12 mx-2 h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" /></svg>
                        </router-link>
                    </div>
                    <div>
                        <p class='text-black my-2 text-lg opacity-50' > #{{room.category_name}} </p>
                        <p class='text-black my-2 text-lg opacity-80 ' >Hosted by @<span class='text-black opacity-90 font-medium' >{{room.host_name}}</span>  </p>
                    </div>
                    <div class=' ' >
                        <router-link :to="{ name: 'Room', params: { code: room.code, title: room.title, description: room.description,   host: room.host, hoster: room.host_name ,  category: room.category_name } }" 
                        class='hover:bg-indigo-700 rounded-md p-2 flex duration-200 bg-gray-200 hover:text-white text-gray-400 text-xl' 
                        >
                            <button class='right-0' >Join</button>
                        </router-link>
                    </div>
                </div>
        
                

                <!-- </router-link> -->
            </div>
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
        code: this.$route.params.code,
       
      }
    },
    methods: {
        getRooms() {
            HTTP.get('api/room/')
            .then((res) => {
                // console.log(res.data)
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
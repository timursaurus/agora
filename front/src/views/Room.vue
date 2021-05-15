<template>
    <div>
        <div>
            <h1>INSIDE ROOM {{ code }} </h1>
            <h1>TITLE {{ title }} </h1>
            <h1>description {{ description }} </h1>
            <h1>Host {{ hoster }} </h1>
            <h1>category {{ category }} </h1>
        </div>
        <button @click='editmode = !editmode' class='bg-indigo-700 w-10 h-6 text-lg ' > Edit </button>
        <div v-if='editmode' class='bg-gray-100' >
            <input v-model='room.title' >
            <textarea v-model='room.description' ></textarea>
            <button @click='saveRoom' > Save </button>
        </div>
    </div>
</template>

<script>
import HTTP from '@/api'
import router from '@/router'
export default {
    props: ['code', 'title', 'description', 'host', 'category','hoster' ],
    data(){
        return {
            room: {
                title: '',
                description: '',
                host: ''
            },
            editmode: false
        }
    },
    components: {
        
    },
    methods: {
        roomInfo() {
            this.room.title = this.title
            this.room.description = this.description
            this.room.host = this.host
        },
        saveRoom() {
            let data = this.room
            console.log(this.room)
            HTTP.put('api/room/edit/' + this.code, data)
            .then(() => {
                router.push('/')
            })

        }
    },
    mounted() {
        this.roomInfo()
    },
}
</script>

<style>

</style>
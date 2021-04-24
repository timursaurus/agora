<template>
    <div class='bg-nicegray border-b' >
        <div class="container mx-auto px-10">
            <div class="grid grid-cols-12 py-2 ">
                    <div class='col-span-3 block w-40 flex items-center '>
                        <h1 class='text-white text-3xl'>Agora</h1>
                    </div>
                    <div class='col-span-6 block' >
                        <div class="relative">
                            <div class='absolute top-0 right-0 h-full w-12 flex justify-center items-center ' >
                                <svg class="h-6 w-6 text-gray-400"  xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd" /></svg>
                            </div>
                            <input class='w-full text-white bg-nicegray-light pr-8 rounded-md h-12 px-4 focus:outline-none text-lg placeholder-gray-400' placeholder='Search' type="text">
                        </div>
                    </div>
                    <div class='col-span-3' >
                        <h1>user</h1>
                    </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return{

        }
    },
    
}

</script>

<style>

</style>
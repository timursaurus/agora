<template>
  <div>
      <div>
          <form class='bg-white py-8 px-6 shadow rounded-lg'>
              <div>
                  <label for='username' class='block text-gray-700 text-sm font-medium '>Username</label>
                  <div>
                      <input 
                      class='border border-gray-300 px-3 py-2 rounded-lg shadow-sm focus:outline-none focus:border-indigo-500' 
                      id='username' name='username' required >
                  </div> 
              </div>
              <div>
                  <label for="password" class='block text-gray-700 text-sm font-medium' >Password</label>
                  <div>
                      <input class='border border-gray-300 px-3 py-2 rounded-lg shadow-sm focus:outline-none focus:border-indigo-500' 
                      id='password' name='password' required>
                  </div>
              </div>
              <div class='mt-3'>
                  <button class='block bg-red-100' >Sign in</button>
              </div>
          </form>
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
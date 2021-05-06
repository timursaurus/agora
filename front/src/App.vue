<template>
  <div id='app' class='min-h-screen text-md'>
    <Nav />
    <router-view v-slot="{Component}" >
      <transition name='route' mode='out-in' >
        <component :is='Component' ></component>
      </transition>
    </router-view>
  </div>
</template>

<script>
import Nav from '@/components/Nav'
export default {
  name: 'App',
  components: {
    Nav,
  }

}
</script>

<style>

.route-enter-from {
  /* opacity: 0;
  transform: translateX(20px) */
}
.route-enter-active {
  transition: all .2s ease;
}
.route-leave-to {
  /* opacity: 0;
  transform: translateX(-20px) */
}




</style>

<template>
  <div>
    <Filters />
    <div>
      <Rooms />
    </div>
    <Footer />
  </div>
</template>

<script>
import Filters from '@/components/Filters';
import Rooms from '@/components/Rooms';
import Footer from '@/components/Footer';
export default {
  name: 'Home',
  data() {},
  components: {
    Filters,
    Rooms,
    Footer,
  },
};
</script>

<style>
</style>
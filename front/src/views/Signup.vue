<template>
  <div>
    <div class="bg-white py-8 px-6 shadow rounded-lg">
      <form class="">
        <div>
          <label for="username" class="block text-gray-700">Username</label>
          <div>
            <input id="username" required />
          </div>
        </div>
        <div>
          <label for="password">Password</label>
        </div>
      </form>
      <h1>lol</h1>
    </div>
  </div>
</template>

<script>
import HTTP from '@/api';

export default {
  name: 'Signup',
  data() {
    return {
      email: '',
      username: '',
      display_name: '',
      password: '',
      ver_password: '',
      errors: [],
    };
  },
  methods: {
    submitForm() {
      this.errors = [];

      if (this.username === '') {
        this.errors.push('Username is missing');
      }

      if (this.password !== this.ver_password) {
        this.errors.push("Passwords don't match ");
      }

      if (this.password === '') {
        this.errors.push('Password is missing');
      }

      if (!this.errors.length) {
        let data = {
          username: this.username,
          password: this.password,
        };

        HTTP.post('', data).then((res) => {
          console.log(res);
        });
      }
    },
  },
};
</script>

<style>
</style>
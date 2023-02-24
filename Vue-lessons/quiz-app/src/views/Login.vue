<template>
  <Box>
    <template #title>
      <span>Login</span>
    </template>
    <form>
      <div class="field">
        <label class="label">Your username</label>
        <input type="name" name="username" placeholder="username" required />
      </div>
        <div class="field">
            <label class="label">Your password</label>
            <input type="password" name="password" placeholder="password" required />

        </div>
      <button class="button">Login</button>
    </form>
    <p class="t-center">
      Need an account? <router-link :to="{ name: 'Register' }">Register</router-link>
    </p>
  </Box>
</template>
  <script>
import Box from "@/components/main/Box.vue";
export default {
  name: "LoginView",
  components: {
    Box,
  },
  data() {
    return {
      context: {
        user: this.$store.state.user,
      },
    };
  },
};
</script>
<template>
  <Box>
    <template #title>
      <span>Register</span>
    </template>
    <form>
      <div class="field">
        <label class="label">Your full name</label>
        <input type="name" name="name" placeholder="John Doe" required />
      </div>
      <div class="field">
        <label class="label">Pick a new username</label>
        <input type="name" name="username" placeholder="username" required />
      </div>
      <div class="field">
        <label class="label">Your Email here</label>
        <input
          type="email"
          name="email"
          placeholder="example@mail.com"
          required
        />
      </div>
      <button class="button">Register</button>
    </form>
    <p class="t-center">
        Have an account? <router-link :to="{ name: 'Login' }">Login</router-link>
    </p>
  </Box>
</template>

<style>
    form + p {
        text-align: center;
        margin-top: 10px;
    }

    form + p a{
        color: var(--light-body-background);
        text-decoration: none;
        font-size: 18px;
    }
</style>
<script>
import Box from "@/components/main/Box.vue";


export default {
  name: "RegisterView",
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
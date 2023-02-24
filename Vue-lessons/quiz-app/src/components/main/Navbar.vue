<template>
  <div class="navbar">
    <div class="nav-logo">
      <router-link :to="{ name: 'Welcome' }">Quiz</router-link>
    </div>
    <div class="action">
      <div v-if="context.user.is_authenticated">
        <button class="button primary">
          <span class="fas fa-user">+</span>
        </button>
      </div>
      <div v-else>
        <router-link to="/login">
          <button class="button primary">
            <span class="fas fa-sign-in-alt">Login</span>
          </button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      context: {
        user: this.$store.state.user,
      },
    };
  },
};
</script>
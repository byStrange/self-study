<template>
  <Navbar></Navbar>
  <router-view></router-view>
  <Footer></Footer>
</template>


<script>
import Navbar from "./components/main/Navbar";
import Footer from "./components/main/Footer";
export default {
  name: "App",
  components: {
    Navbar,
    Footer,
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
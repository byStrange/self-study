<template>
  <Composition title="composition" />
  <router-view />
</template>

<script>
import Composition from "./components/Composition.vue";
export default {
  components: {
    Composition,
  },
  setup() {},
};
</script>

<style lang="stylus">
body {
  background: #151515;
  color: #fff;
  font-family: Poppins;
  font-size: 25px;
}
</style>

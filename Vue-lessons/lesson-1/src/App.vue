<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <div v-bind:class="center">
    {{ counter }}
  </div>
  <MinusBtn btn="-" v-on:click="minus" ref="plusBtn" />
  <PlusBtn buttonName="+" v-on:click="plus" ref="plusBtn" />
  <!-- <ToZeroBtn name="clear" v-on:click="Null" /> -->
</template>

<script>
import MinusBtn from "./components/minusBtn.vue";
import PlusBtn from "./components/plustBtn.vue";
export default {
  components: {
    MinusBtn,
    PlusBtn,
  },
  name: "App",
  data() {
    return {
      center: "center",
      counter: 0,
    };
  },
  mounted() {
    console.log(this.$refs.plusBtn, 'refs');
    // get the text inside the button
    console.log(this.$refs.plusBtn.buttonName, 'refs');
  },
  methods: {
    plus() {
      this.counter += 1;
    },
    minus() {
      this.counter -= 1;
    },
  },
};
window.oncontextmenu = function () {
  return false;
};
window.onload = function () {
  document.body.requestFullscreen();
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
  user-select: none;
  transition: 250ms;
}
#app {
  position: relative;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  /* margin-top: 60px; */
  width: 100%;
  height: 100vh;
}
.center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: poppins;
  font-size: 12em;
}
button {
  border: none;
  padding: 8px 14px;
  background: rgba(0, 0, 0, 0.4);
  color: #fff;
  border: 1px solid #2c3e50;
  border-radius: 8px;
  cursor: pointer;
  margin-left: 20px;
}
.side {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 100px;
  color: #fff;
}
.side:hover {
  font-size: 150px;
}
</style>

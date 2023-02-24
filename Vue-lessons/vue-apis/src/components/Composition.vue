<template>
  <div class="title">
    <p>Title from Composition.vue : {{ title }}</p>
    <p>{{ message }}</p>
    <div>
        <input type="text" v-model="message">
    </div>
</div>
</template>

<script>
import { ref } from "@vue/reactivity";
export default {
  name: "Composition",
  props: {
    title: {
      type: String,
      default: "Hello World",
    },
  },
  setup(props) {
    const message = ref("Hello world")
    function changeMessage(d) {
        message.value = d;
    }
    console.log(message)
    console.log(message.value)
    return {
        message
    }
  },
};
</script>

<style lang="stylus"></style>
<template>
  <Box>
    <template #title>
      <span>Welcome to Quiz</span>
    </template>
    <p>
      Quiz is a simple quiz application that allows you to create and take
      quizzes. You will be able to create quizzes and share them with your
      friends. You can also take quizzes created by other users.
    </p>

    <div class="mt-1">
      <router-link to="/more" class="mt-1">Learn more</router-link>
    </div>
    <p class="mt-1">
      <router-link :to="{ name: 'Register' }">
        <button class="button primary">
          <span class="fas fa-user-plus"></span>Register Now
        </button>
      </router-link>
    </p>
  </Box>
</template>

<style>
.highlited.marked {
  position: relative;
  color: #000 !important;
}
.highlited.marked::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: var(--light-body-background);
  opacity: 0.5;
}
.highlited.marked.left::after {
  transform: scale(1.05) rotate(-3deg);
}
.highlited.marked.right::after {
  transform: scale(1.05) rotate(3deg);
}
</style>

<script>
import { saveAs } from 'file-saver';
import Box from "@/components/main/Box.vue";
import anime from "animejs";
var FileSaver = require('file-saver');
var blob = new Blob(["Hello, world!"], {type: "text/plain;charset=utf-8"});
FileSaver.saveAs(blob, "hello world.txt");
export default {
  name: "WelcomeView",
  components: {
    Box,
    Box,
  },
  data() {
    return {
      context: {
        user: this.$store.state.user,
      },
    };
  },
  methods: {},
  // create a function that calls automatically when loading the page
};
</script>
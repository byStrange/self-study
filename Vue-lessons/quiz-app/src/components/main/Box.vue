<template>
  <div class="container">
    <div class="quiz-box">
      <div class="quiz-title p-relative">
        <slot name="title"></slot>
      </div>
      <div class="content">
        <slot></slot>
      </div>
    </div>
  </div>
</template>
 
<script>
export default {
  name: "Box",
};
</script>
<template>
    <footer class="footer">
        <p>
            Made with <span class="fas fa-heart"></span> by <a class="link" href="//github.com/byStrange/">Rakhmatullo</a>
        </p>
    </footer>    
</template>

<style>
    footer {
        width: 100vw;
        position: fixed;
        bottom: 0;
        padding: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        background: rgba(255, 255, 255, 0.5);
        filter: blur(1px)
    }
</style>

<script>
    export default {
        name: "Footer",
    }
</script>

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/root.css'
import './index.css'
import { createStore } from "vuex";

const store = createStore({
    state() {
        return {
            user: {
                is_authenticated: false,
                is_new: true
            }
        }
    }
});

createApp(App).use(router).use(store).mount('#app')

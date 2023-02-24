import { createRouter, createWebHistory } from "vue-router";
import TestRouter from "@/components/Test";
const routes = [
  {
    path: "/test",
    component: TestRouter,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import GeoIp from "../views/GeoIp.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/ip",
    name: "GeoIp",
    component: GeoIp
  }
];

const router = new VueRouter({
  mode: "abstract",
  base: process.env.BASE_URL,
  routes
});

export default router;

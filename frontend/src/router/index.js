import { createWebHistory, createRouter } from "vue-router";

import appChildren from "./children/app-children";

const Homepage = () =>
  import(/* webpackChunkName: "Homepage" */ "@/components/Homepage");

const routes = [
  {
    path: "/",
    name: "Home",
    component: Homepage,
    children: appChildren,
    // beforeEnter: async (to, from, next) => {
    //   next();
    // },
  },
];


const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  
export default router;
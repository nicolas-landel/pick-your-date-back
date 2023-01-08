import { createWebHistory, createRouter } from "vue-router";

// import appChildren from "./children/app-children";


const Homepage = () => import("@/components/Homepage.vue")
const Dashboard = () => import("@/components/Dashboard.vue")

const routes = [
  {
    path: "/",
    name: "home",
    component: Homepage,
    meta: {
      public: true,
    }
    // children: appChildren,
    // beforeEnter: async (to, from, next) => {
    //   next({ name: "connection" });
    //   // if (store.getters["user/isLogged"]) {
    //   //   next({ name: "dashboard" });
    //   // } else {
    //   //   next({ name: "connection" });
    //   // }
    // },
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: Dashboard,
    // children: dashboardChildren,
  },
  {
    path: "/:catchAll(.*)",
    component: Homepage,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

const Dashboard = () => import("@/components/app/Dashboard.vue")



export default [
  {
    path: "/dashboard",
    name: "dashboard",
    components: Dashboard,
    // children: dashboardChildren,
  }

]
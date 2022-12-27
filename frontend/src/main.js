import { createApp } from "vue";
import App from './App.vue'
// import i18n from "./setup/i18n";
// import vuetify from "./setup/vuetify";
import router from "./router";
// import store from "./store";


const app = createApp(App);
app.use(router).mount("#app")

// console.log("HHHHH", Vue)

// new Vue({
//   router,
//   // store,
//   // i18n,
//   vuetify,
//   render: (h) => h(App),
// }).$mount("#app");

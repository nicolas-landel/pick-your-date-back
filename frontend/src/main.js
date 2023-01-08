import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import i18n from '@/setup/i18n'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
  components,
  directives,
})



const vue = createApp(App);
vue.use(router);
vue.use(store);
vue.use(vuetify);
vue.use(i18n);

vue.mount("#app");

// Run!
// router.isReady().then(() => {
//   vue.mount('#app');
// });
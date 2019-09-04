import "./plugins/vuetify";
import "./registerServiceWorker";

import router from "@/router";
import store from "@/store/store";
import Vue from "vue";

import App from "./App.vue";
import Vuetify from 'vuetify';

Vue.use(Vuetify, {
  iconfont: 'mdi'
})


Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");


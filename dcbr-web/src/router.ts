import Vue from "vue";
import Router from "vue-router";

import Home from "./views/Home.vue";
import OperationRegistration from "./views/OperationRegistration.vue";
import Preamble from "./views/Preamble.vue";
import Payment from "./views/Payment.vue";
import Review from "./views/Review.vue";
import Confirmation from "./views/Confirmation.vue";



Vue.use(Router);

// export default new Router({
//   mode: 'history',
//   base: process.env.BASE_URL,
//   routes: [],
// });

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/preamble",
      name: "preamble",
      component: () =>
        // import(/* webpackChunkName: "secret" */ "./views/Secret.vue"),
        import("./views/Preamble.vue"),
      meta: {
        requiresAuth: false
      }
    },
    {
      path: "/register",
      name: "register",
      // component: () =>
      //   import(
      //     /* webpackChunkName: "register" */ "./views/OperatorRegistration.vue"
      //   ),
      //   import("./views/OperatorRegistration.vue"),
      // meta: {
      //   requiresAuth: false
      // }
      component: OperationRegistration
    },
    {
      path: "/payment",
      name: "payment",
      component: () =>
        // import(/* webpackChunkName: "secret" */ "./views/Secret.vue"),
        import("./views/Payment.vue"),
      meta: {
        requiresAuth: false
      }
    },
    {
      path: "/review",
      name: "review",
      component: () =>
        // import(/* webpackChunkName: "secret" */ "./views/Secret.vue"),
        import("./views/Review.vue"),
      meta: {
        requiresAuth: false
      }
    },
    {
      path: "/confirmation",
      name: "confirmation",
      component: () =>
        // import(/* webpackChunkName: "secret" */ "./views/Secret.vue"),
        import("./views/Confirmation.vue"),
      meta: {
        requiresAuth: false
      }
    },

    {
      path: "/dashboard",
      name: "dashboard",
      component: () =>
        // import(/* webpackChunkName: "secret" */ "./views/Secret.vue"),
        import("./views/OperatorDash.vue"),
      meta: {
        requiresAuth: false
      }
    }
  ]
});

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requiresAuth)) {
//     if (router.app.$keycloak.authenticated) {
//       next();
//     } else {
//       const loginUrl = router.app.$keycloak.createLoginUrl();
//       window.location.replace(loginUrl);
//     }
//   } else {
//     next();
//   }
// });

export default router;

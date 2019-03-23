// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'

import store from './store/index'
import api from './api'
// import 'vuetify/dist/vuetify.min.css'
import VueTyper from 'vue-typer'

Vue.config.productionTip = false

Vue.use(Vuetify)
Vue.use(api)
Vue.use(VueTyper)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>',
})

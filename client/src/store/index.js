import Vue from 'vue'
import Vuex from 'Vuex'
import client from "@/api";
import router from "@/router"

Vue.use(Vuex)

export default new Vuex.Store({
  state:{
    isLoggedIn: false,
    isShowLoginModal: false,
    isShowSignupModal: false,
    backgroundImg: require('@/assets/background.jpeg'),
    topContent: [
      {
       'title':'自動フォロー',
        'body':'AIが御社の求人条件を解析、有望な採用候補者をTwitter上で自動フォローします',
        'img':require('@/assets/follow.png')
      },
      {
        'title':'自動リストアップ',
        'body':'AIが有望な採用候補者を自動でリストアップ、優先順位を表示します',
        'img':require('@/assets/white_list.png')
      },
      {
        'title':'自動スカウト',
        'body':'AIが御社の希望に基づき自動でスカウトDMを配信、エントリーへ誘導します',
        'img':require('@/assets/scout.png')
      },
    ]
  },
  mutations: {
    loggedIn (state, token) {
      state.isLoggedIn = true
      client.defaults.headers.common['Authorization'] = `JWT ${token}`
      localStorage.setItem('token', token)
    },
    loggedOut (state) {
      state.isLoggedIn = false
      delete client.defaults.headers.common['Authorization']
      localStorage.clear()
      router.push('/')
    },
    showLoginModal(state){
      state.isShowLoginModal = true
    },
    showSignupModal(state){
      state.isShowSignupModal = true
    },
    hide(state){
      state.isShowLoginModal = false
      state.isShowSignupModal = false
    }
  },
  actions: {
    login ({commit}, [username, password]){
      return client.auth.login(username, password).then(res => {
        commit('loggedIn', res.data.token)
        return res
      })
    },
    signup ({commit}, [username, email, password]){
      return client.auth.signup(username, email, password).then(res => {
        commit('loggedIn', res.data.token)
        return res
      })
    },
    logout ({commit}){
      commit('loggedOut')
    },
    showLoginModal({commit}){
      commit('showLoginModal')
    },
    showSignupModal({commit}){
      commit('showSignupModal')
    },
    hideModal({commit}){
      commit('hide')
    },
    tryLoggedIn({commit}){
      const token = localStorage.getItem('token')
      if (token) {
        client.auth.verify(token).then(() => {
          commit('loggedIn', token)
        }, () => {
          localStorage.clear()
        })
      }
    },
  },
  getters: {
    isLoggedIn(state){
      return state.isLoggedIn
    },
    getShowLoginModal(state){
      return state.isShowLoginModal
    },
    getShowSignupModal(state){
      return state.isShowSignupModal
    },
    getBackgroundImg(state){
      return state.backgroundImg
    },
    getTopContent(state){
      return state.topContent
    }
  }
})

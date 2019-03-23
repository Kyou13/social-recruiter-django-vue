<template>
  <v-app id="app">
    <router-view/>
  </v-app>
</template>

<script>
  import {mapActions, mapGetters} from 'vuex'

  export default {
    name: 'App',
    created() {
      this.$store.dispatch('tryLoggedIn')
    },
  }
</script>

<style>
#app {
  font-family: Roboto, "ヒラギノ角ゴ Pro W3", "Hiragino Kaku Gothic Pro", "メイリオ", "Lucida Grande", Verdana, "ＭＳ Ｐゴシック", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #323232;
  background-color: #fff;
  font-size: 16px;
}
  body{
    margin: 0;
  }
</style>

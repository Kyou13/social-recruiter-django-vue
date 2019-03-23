<template>
  <header>
    <nav>
      <ul>
        <li>
          <v-btn outline round class="grey" active-class="white" to="/">トップ</v-btn>
        </li>
        <li>
          <v-btn outline round class="blue" v-show="!isLoggedIn" @click="showLoginModal">ログイン</v-btn>
        </li>
      </ul>
    </nav>
  </header>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import LoginModal from '@/components/LoginModal'

  export default {
    name: 'HeadComp',
    components:{
      LoginModal
    },
    computed: {
      ...mapGetters({
        'isLoggedIn': 'isLoggedIn',
      })
    },
    methods: {
      ...mapActions([
        'login',
        'logout',
        'tryLoggedIn',
        'showLoginModal'
      ])
    }
  }
</script>

<style scoped>
  header{
    width: 900px;
    height: 40px;
    margin: 25px auto;
    z-index: 2;
    text-align: right;
  }
  nav{
    float: right;
  }
</style>

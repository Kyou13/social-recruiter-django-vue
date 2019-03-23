<template>
  <footer class="grey darken-4">
    <v-container>
      <ul class="mb-5">
        <li>
          <router-link  to="/" class="white--text">トップ</router-link>
        </li>
        <li>
          <router-link  to="/" class="white--text">ヘルプ</router-link>
        </li>
        <li>
          <router-link  to="/" class="white--text">会社概要</router-link>
        </li>
      </ul>
      <hr>
      <div class="company-name white--text mt-4">株式会社dip</div>
    </v-container>
  </footer>
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
  footer{
    text-align: left;
  }
  li a:link{
    text-decoration: none;
  }
  .company-name{
    margin-left: 10px;
  }
  footer hr{
    border: solid rgba(255,255,255,.2);
    border-width: 1px 0 0;
  }
</style>

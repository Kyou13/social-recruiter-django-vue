<template>
  <div>
    <head-comp></head-comp>
    <v-layout>
      <v-container>
        <login-modal v-if="getShowLoginModal"></login-modal>
        <signup-modal v-if="getShowSignupModal"></signup-modal>
        <v-parallax :src="getBackgroundImg" class="mb-4">
          <v-layout align-center column justify-center>
            <h1 class="display-4 mb-3">
              Social Recruiter
            </h1>
            <h4 class="headline">
              勝手に応募者が集まってくる夢のツール！<br/>
              企業の採用アカウント運用自動化します
            </h4>
          </v-layout>
        </v-parallax>
        <v-flex xs12 class="mb-3">
          <h3 class="display-2 mb-3">How It Work?</h3>
          <div class="subheading">Social Recruiterは人事のTwitter運用を自動化します</div>
        </v-flex>
        <v-layout row wrap align-center v-for="(element, index) in  getTopContent">
          <v-flex xs12 md6>
            <h4 class="headline text-xs-left">{{ element.title }}</h4>
            <div class="body-1 text-xs-left">{{ element.body }}</div>
          </v-flex>
          <v-flex xs12 md6>
            <v-layout justify-center>
              <v-img :src=element.img max-width="50%"></v-img>
            </v-layout>
          </v-flex>
        </v-layout>
      </v-container>
    </v-layout>
    <fotter-comp></fotter-comp>
  </div>
</template>

<script>
  import HeadComp from '@/components/HeadComp'
  import FotterComp from '@/components/FotterComp'
  import LoginModal from '@/components/LoginModal'
  import SignupModal from '@/components/SignupModal'
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'Top',
    created() {
      this.$store.dispatch('hideModal')
    },
    components: {
      HeadComp,
      FotterComp,
      LoginModal,
      SignupModal,
    },
    computed: {
      ...mapGetters([
        'getShowLoginModal',
        'getShowSignupModal',
        'getBackgroundImg',
        'getTopContent'
      ])
    }
  }
</script>

<style>
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
  .top-title{
    text-align: center;
  }
</style>

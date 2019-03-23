<template>
  <div>
    <h2 class="modal-title">
      ログイン
    </h2>
    <v-alert :value="nonFieldErrors.length" type="error">
      <div v-for="error in nonFieldErrors" :key="error">{{ error }}</div>
    </v-alert>
    <v-form v-model="valid">
      <v-text-field
        v-model="username"
        label="ログインID"
        :rules="usernameRules"
        required></v-text-field>
      <v-text-field
        v-model="password"
        label="パスワード"
        :append-icon="showPassword ? 'visibility' : 'visibility_off'"
        :append-icon-cb="() => (showPassword = !showPassword)"
        :type="showPassword ? 'text' : 'password'"
        :rules="passwordRules"
        required></v-text-field>
      <v-btn :disabled="!valid" @click="submit">ログイン</v-btn>
    </v-form>

  </div>
</template>

<script>
  import {mapActions} from 'vuex'
  import axios from 'axios'

  export default {
    name: 'Login',
    data (){
      return{
        valid: false,
        username: null,
        password: null,
        showPassword: false,
        nonFieldErrors: [],
        usernameRules: [
          v => !!v || 'ログインIDを入力してください',
        ],
        passwordRules: [
          v => !!v || 'パスワードを入力してください',
        ]
      }
    },
    methods: {
      ...mapActions(['login', 'hideModal']),
      submit () {
        this.nonFieldErrors = []
        this.login([this.username, this.password]).then(res => {
          this.$router.push('/dashboard')
      }, err => {
        this.nonFieldErrors = err.response.data.nonFieldErrors
        })
      }
    }
  }
</script>

<style scoped>
  .modal-mask {
    position: fixed;
    z-index: 9998;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.1);
    display: table;
    transition: opacity .3s ease;
  }

  .modal-wrapper {
    display: table-cell;
    vertical-align: middle;
  }

  .modal-container {
    width: 300px;
    margin: 0px auto;
    padding: 20px 30px;
    background-color: #fff;
    border-radius: 2px;
    transition: all .3s ease;
    font-family: Helvetica, Arial, sans-serif;
  }

  .modal-title{
    color: #beb5fc;
  }

  .modal-enter .modal-container,
  .modal-leave-active .modal-container {
    -webkit-transform: scale(1.1);
    transform: scale(1.1);
  }

  img{
    width: 100%;
  }
  .modal-close-button{
    text-decoration: none;
    color: #beb5fc;
    padding: 5px;
    border-radius: 5px;
    border: solid 2px #beb5fc;
    text-align: center;
    vertical-align: middle;
    overflow: hidden;
    font-weight: bold;
    transition: .4s;
    cursor: pointer;
  }
  .modal-close-button:hover{
    background: #d2cafc;
  }
</style>

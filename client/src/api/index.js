import axios from 'axios'
import auth from './auth'

const client = axios.create({
  baseURL: "http://localhost:8000/",
})

client.auth = auth(client)

client.install = function (Vue) {
  Object.defineProperty(Vue.prototype, '$request', {
    get () {
      return client
    },
  })
}

export default client

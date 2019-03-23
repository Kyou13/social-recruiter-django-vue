export default function (cli) {
  return {
    login (username, password) {
      const data = {
        username,
        password,
      }
      return cli.post('login/', data)
    },
    signup(username, email, password) {
      const data = {
        username,
        email,
        password,
      }
      return cli.post('/register/' , data)
    },
    verify(token){
      return cli.post('auth/verify/', {token})
    }
  }
}

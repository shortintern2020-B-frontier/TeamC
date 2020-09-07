import axios from 'axios'

export default {
  created: function () {
    axios.get('http://127.0.0.1:8000/user/find/1')
      .then(response => {
        console.log(response.data) // mockData
        console.log(response.status) // 200
      })
  }
}
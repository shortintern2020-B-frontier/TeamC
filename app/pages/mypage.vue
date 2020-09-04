
<script>
  import axios from 'axios'
  export default {
    created: function () {
      axios.get('http://127.0.0.1:8000/users/find?id=2')
        .then(response => {
          console.log(response.data) // mockData
          console.log(response.status) // 200
        })
    }
}
</script>
<template>
  <form>
    <div id="profile">
      <div id="icon">
        <v-avatar>
          <img src="@/static/v.png">
        </v-avatar>
          <v-btn>画像を変更する</v-btn>
      </div>
      <v-text-field
        v-model="userId"
        :counter="10"
        label="ID"
        placeholder="userid"
        required
      ></v-text-field>
      <v-text-field
        v-model="name"
        label="Name"
        placeholder="太郎"
        required
      ></v-text-field>
      <v-text-field
        v-model="email"
        label="E-mail"
        placeholder="example@gmail.com"
      ></v-text-field>

      <v-text-field
        v-model="birstday"
        label="Birth Day"
        placeholder="2020/1/1"
      ></v-text-field>
      <v-text-field
        v-model="comment"
        label="Comment"
        placeholder="コメント"
        
      ></v-text-field>
    </div>
    <div id="status">
      <h1>Status</h1>

    </div>
  </form>
</template>
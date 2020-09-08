<!-- Author Hiroki Okubo -->

<template>
  <div class="container">
   <table border="1">
     <tbody>
     <tr>
       <th>ID</th>
       <th>タイムライン</th>
     </tr>
     <tr v-for="item in items" :key="item.id">
       <td>{{ item.id }}</td>
       <td>{{ item.name }}</td>
     </tr>
     </tbody>
   </table>
 </div>
</template>



<!-- 遷移ページ -->
<!-- export default {
  created(){
  this.chats = await this.$axios.get(`/chats/${this.id}`);
}
} -->

<script>
export default {
  data() {
    return {
      items: []
    }
  },
  mounted: function() {
    this.$axios
      // .$get('/timelines')
       // http://127.0.0.1:8000/users/login
      .$post('/users/login')
      .then(response => {
        this.items = response
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>

<!-- from Hirata-san
database からデータを取る

async created() {
  this.timelines = await this.$axios.get(`/timelines?user_id=${this.user_id}`);
} -->

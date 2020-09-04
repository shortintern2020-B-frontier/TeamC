
<script>
  export default {
    async asyncData({ $axios }) {
    const data = await $axios.$get('/users/', {params: "user_id"})
    console.log(data[0])
    return { data }
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
        placeholder="user_id"
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
<template>
  <form>
    <div id="app">
      <div id="icon">
        <v-avatar>
          <img src="@/static/v.png" />
        </v-avatar>
        <v-btn @click="setImg">画像を変更する</v-btn>
      </div>
      <v-text-field v-model="user_id" :counter="10" label="ID" required></v-text-field>
      <v-text-field v-model="username" label="Name" required></v-text-field>
      <v-text-field v-model="email" label="E-mail" required></v-text-field>
      <v-btn @click="postProfile">プロフィールを更新する</v-btn>
    </div>
    <div id="status">
      <h1>Status</h1>
      <v-text-field v-model="comment" label="Comment"></v-text-field>
      <div id="components-demo">
        <Status></Status>
      </div>
    </div>
  </form>
</template>

<script>
import Vue from "vue";
import Status from "~/components/Status";

Vue.component("Status", Status);
export default {
  name: "mypage",
  async asyncData({ $axios }) {
    const data = await $axios.$get("/users/find", {
      params: { user_id: "string" },
    });
    return data;
  },
  methods: {
    setUserId: function () {},

    createJson: function (key, value) {
      var json;
      return (json[key] = value);
    },
    postProfile: async function () {
      console.log(this.id);
      var json;
      await this.$axios.$post("/users/update", {
        user_id: this.user_id,
        username: this.username,
        email: this.email,
        password: this.password,
        status: 0,
        comment: this.comment,
      });
    },
  },
  mounted: function () {},
};
</script>


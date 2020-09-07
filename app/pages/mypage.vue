<template>
  <form>
    <div id="profile">
      <div id="icon">
        <v-avatar>
          <img src="@/static/v.png" />
        </v-avatar>
        <v-btn>画像を変更する</v-btn>
      </div>
      <v-text-field v-model="user_id" :counter="10" label="ID" required></v-text-field>
      <v-text-field v-model="username" label="Name" required></v-text-field>
      <v-text-field v-model="email" label="E-mail" required></v-text-field>
      <v-btn @click="postProfile">プロフィールを更新する</v-btn>
    </div>
    <div id="status">
      <h1>Status</h1>
      <v-text-field v-model="comment" label="Comment"></v-text-field>
      <Status />
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
    postProfile: async function () {
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


<!-- Author:Shotaro Murata-->
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
    </div>
    <div id="status">
      <h2>Status</h2>
      <v-text-field v-model="comment" label="Comment"></v-text-field>
      <input type="radio" id="free" value="0" v-model="status" />
      <label>Free</label>
      <br />
      <input type="radio" id="busy" value="1" v-model="status" />
      <label>Busy</label>
    </div>
    <v-btn @click="postProfile">プロフィールを更新する</v-btn>
  </form>
</template>

<script>
import Vue from "vue";

export default {
  name: "mypage",
  layout: "mypage",
  components: {},
  async asyncData({ $axios }) {
    const data = await $axios.$get("/users/find", {
      params: { user_id: "user_id" },
    });
    return data;
  },
  methods: {
    postProfile: async function () {
      await this.$axios.$post("/users/update", {
        id: 1,
        user_id: this.user_id,
        username: this.username,
        email: this.email,
        status: this.status,
        comment: this.comment,
      });
    },
  },
  computed: {},
  mounted: function () {},
};
</script>


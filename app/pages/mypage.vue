<!-- Author:Shotaro Murata-->
<template>
  <v-app>
    <v-main style="margin:5%;">
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
          <ul id="example-1">
            <div v-for="item in statusList" :key="item.id">
              <input type="radio" v-bind:id="item.id" v-bind:value="item.id" v-model="status" />
              <i v-bind:class="item.class" />
              <label>{{item.title}}</label>
            </div>
          </ul>
        </div>
        <v-btn @click="postProfile">プロフィールを更新する</v-btn>
      </form>
    </v-main>
  </v-app>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "mypage",
  layout: "default",
  components: {},
  data: {
    statusList: [],
  },
  async asyncData({ store }) {
    return store.state.user.userInfo;
  },
  methods: {
    postProfile: async function () {
      await this.$axios.$post("/users/update", {
        id: this.$store.state.user.userInfo.id,
        user_id: this.user_id,
        username: this.username,
        email: this.email,
        status: this.status,
        comment: this.comment,
      });
    },
  },
  computed: mapState("user", ["statusList"]),
};
</script>


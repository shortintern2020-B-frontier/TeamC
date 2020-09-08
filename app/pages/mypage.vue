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
          <input type="radio" id="free" value="0" v-model="status" />
          <label>Free</label>
          <br />
          <input type="radio" id="busy" value="1" v-model="status" />
          <label>Busy</label>
        </div>
        <v-btn @click="postProfile">プロフィールを更新する</v-btn>
      </form>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "mypage",
  layout: "default",
  components: {},
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
  computed: {},
  mounted: function () {},
};
</script>


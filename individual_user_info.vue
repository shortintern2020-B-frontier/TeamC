<!-- Author Hiroki Okubo -->

<template>
  <div>
    <v-app
      <!-- <v-main style="margin-left: 50%; margin-top:100px"> -->
      <v-main style="margin-top:100px; text-align:center;">

  <img style="margin-left: 30%;" class="img" src="/v.png" width="50%" />
  <!-- <img style="text-align:center;" class="img" src="/v.png" width="50%" /> -->

  <v-text>Bob-san</v-text>
  <!-- <v-text>friend_data.username</v-text> -->
  <span>{{ friend_data.username }}</span>

  <div class="text-center">
      <v-btn small class="ma-2" outlined color="indigo">chat</v-btn>
      <v-btn small class="ma-2" outlined color="success">favorite</v-btn>
      <v-btn small class="ma-2" outlined color="teal">block</v-btn>
    </div>

</v-main>
</v-app>

</div>
</template>

<script>
export default {
  layout: "home",
  data: () => ({
    friend_data: [],
  }),
  methods: {
    findData: async function() {
      // let userid = this.$store.state.user.userInfo.id; //友達のuserid

      const friend_data = this.$axios.get('/users/find', {
        params: {
          // user_id: this.userid,
          // $route.query (もし URL 上にクエリがあるなら)
          user_id: this.$route.query.user_id,
        }
      });
    },
    if (friend_data != null) {
      this.friend_data = friend_data;
    },
    search(keyword) {
      this.searchlist = this.friendslist.filter(
        friend => friend.status == keyword
      );
    }
  },
  created() {
    this.findData();
  }

</script>

<script>
export default {
  data() {
    return {
      staticImage: "/v.png"
    };
  },
};
</script>

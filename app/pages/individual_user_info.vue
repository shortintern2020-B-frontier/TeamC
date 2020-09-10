<!-- Author Hiroki Okubo -->

<template>
  <div>
    <v-app>
      <v-main style="margin-top:100px; text-align:center;">
        <v-avatar class="ma-3" size="70" tile>
          <img :src="avatar(friend_data.id)" :alt="friend_data.username" />
        </v-avatar>
        <span class="headline">{{ friend_data.username }}</span>

        <div class="text-center">
          <v-btn small class="ma-2" outlined color="indigo" @click="postInvite" v-bind:disabled="invited">invite to chat</v-btn>
          <v-btn small class="ma-2" outlined color="success" @click="postFavorite" v-bind:disabled="favorited">favorite</v-btn>
          <!-- <v-btn small class="ma-2" outlined color="teal">block</v-btn> -->
        </div>
      </v-main>
    </v-app>
  </div>
</template>


<script>
export default {
  data: () => ({
    friend_data: {},
    favorited: false,
    invited: false,
  }),
  methods: {
    findData: async function () {
      console.log(this.$route.query.user_id);

      const data = await this.$axios.$get("/users/find", {
        params: {
          // $route.query (もし URL 上にクエリがあるなら)
          user_id: this.$route.query.user_id,
        },
      });
      const favorite = await this.$axios.$get("/users/favorites", {
        params: {
          // $route.query (もし URL 上にクエリがあるなら)
          id: this.$store.state.user.userInfo.id,
        },
      });
      
      if (data != null) {
        this.friend_data = data;
        const invite = await this.$axios.$get("/invites/", {
          params: {
            user_id: this.friend_data.id,
          },
        });
        const matchInvite = invite.filter((n) => n.users[0].id == this.$store.state.user.userInfo.id);
        if(!matchInvite.length){
          this.invited = false
        }else{
          this.invited = true
        }
        const matchFavarite= favorite.filter((n) => n.user_id == this.$route.query.user_id);
        if(!matchFavarite.length){
          this.favorited = false
        }else{
          this.favorited = true
        }
      }
    },
    postFavorite: async function () {
      const data = await this.$axios.$post("/users/favorites", {
        user_id: this.$store.state.user.userInfo.id,
        target_user_id: this.friend_data.id,
      });
      console.log(data);
      if (data != null) {
        this.favorited = true
      }
    },
    postInvite: async function () {
      const data = await this.$axios.$post("/invites/create", {
        host_user_id: this.$store.state.user.userInfo.id,
        guest_user_id: this.friend_data.id,
      });
      console.log(data);
      if (data != null) {
        this.invited = true
      }
    },
  },
  created() {
    this.findData();
  },
  computed: {
    avatar() {
      return (id) => {
        const imageLen = 10;
        return `/user_icon_${(id % imageLen) + 1}.jpg`;
      };
    },
  },
};
</script>
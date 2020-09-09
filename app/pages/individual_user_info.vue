<!-- Author Hiroki Okubo -->

<template>
  <div>
    <v-app>
      <v-main style="margin-top:100px; text-align:center;">

  <img style="margin-left: 30%;" class="img" src="/v.png" width="50%" />

  <!-- <v-text>Bob-san</v-text> -->
  <span v-if="friend_data">{{ friend_data.username }}</span>

  <div class="text-center">
      <v-btn small class="ma-2" outlined color="indigo" @click="postInvite">chat</v-btn>
      <v-btn small class="ma-2" outlined color="success"  @click="postFavorite">favorite</v-btn>
      <!-- <v-btn small class="ma-2" outlined color="teal">block</v-btn> -->
    </div>

</v-main>
</v-app>

</div>
</template>


<script>
export default {
    data:{
      friend_data: null,
      staticImage: "/v.png"
    },
    methods: {
      findData: async function() {

        console.log(this.$route.query.user_id)

        const data = await this.$axios.$get('/users/find', {
          params: {
            // $route.query (もし URL 上にクエリがあるなら)
            user_id: this.$route.query.user_id,
          }
        });
        if (data != null) {
          this.friend_data = data;
        }
        console.log(this.friend_data.username)
      },
      postFavorite: async function() {

        const data = await this.$axios.$post('/users/favorites', {
          user_id: this.$store.state.user.userInfo.id,
          target_user_id: this.friend_data.id
          
        });
        console.log(data)
        if (data != null) {
        }
      },
      postInvite: async function() {

        const data = await this.$axios.$post('/invites/create', {
          host_user_id: this.$store.state.user.userInfo.id,
          guest_user_id: this.friend_data.id
        
        });
        console.log(data)
        if (data != null) {
        }
      },
    },
    created() {
      this.findData();
    }
  }

</script>
<!-- Author Hiroki Okubo -->

<template>
  <div>
    <v-app>
      <v-main style="margin-top:100px; text-align:center;">
        <b-container class="justifiy-content-center">
          <v-col>
            <v-avatar class="ma-3" size="70" tile>
              <img :src="avatar(friend_data.id)" :alt="friend_data.username" />
            </v-avatar>
            <span class="headline">{{ friend_data.username }}</span>
          </v-col>

          <div id="status" style="text-align: center; margin: auto;">
            <v-col style="margin: auto; text-align: center;">
              <v-row style="display: block;">
                <i v-bind:class="getStatusClass(0)" />
                <p>{{getStatusTitle(0)}}</p>
              </v-row>
              <v-row style="display: block;">
                <p>Comment: {{ friend_data.comment }}</p>
              </v-row>
            </v-col>
          </div>

          <div class="text-center">
            <v-btn
              small
              class="ma-2"
              outlined
              color="indigo"
              @click="postInvite"
              v-bind:disabled="invited"
            >invite to chat</v-btn>
            <v-btn
              small
              class="ma-2"
              outlined
              color="success"
              @click="postFavorite"
              v-bind:disabled="favorited"
            >favorite</v-btn>
            <!-- <v-btn small class="ma-2" outlined color="teal">block</v-btn> -->
          </div>
        </b-container>
      </v-main>
    </v-app>
  </div>
</template>


<script>
import { mapState } from "vuex";
export default {
  data: () => ({
    friend_data: {},
    favorited: false,
    invited: false,
    status: {},
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
        console.log(this.friend_data);
        const invite = await this.$axios.$get("/invites/", {
          params: {
            user_id: this.friend_data.id,
          },
        });
        const matchInvite = invite.filter(
          (n) => n.users[0].id == this.$store.state.user.userInfo.id
        );
        if (!matchInvite.length) {
          this.invited = false;
        } else {
          this.invited = true;
        }
        const matchFavarite = favorite.filter(
          (n) => n.user_id == this.$route.query.user_id
        );
        if (!matchFavarite.length) {
          this.favorited = false;
        } else {
          this.favorited = true;
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
        this.favorited = true;
      }
    },
    postInvite: async function () {
      const data = await this.$axios.$post("/invites/create", {
        host_user_id: this.$store.state.user.userInfo.id,
        guest_user_id: this.friend_data.id,
      });
      console.log(data);
      if (data != null) {
        this.invited = true;
      }
    },
    getStatusClass(id) {
      return this.$store.state.user.statusList[id].class;
    },
    getStatusTitle(id) {
      return this.$store.state.user.statusList[id].title;
    },
  },
  created() {
    this.findData();
    this.status = this.$store.state.user.statusList;
  },
  computed: {
    ...mapState("user", ["statusList"]),
    avatar() {
      return (id) => {
        const imageLen = 10;
        return `/user_icon_${(id % imageLen) + 1}.jpg`;
      };
    },
  },
};
</script>
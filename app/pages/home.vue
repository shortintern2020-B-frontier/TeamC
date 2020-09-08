// Author: ZHANG CHI
<template>
  <v-app>
    <v-main>
      <!-- <v-app-bar color="" dense></v-app-bar> -->
      <v-container class="fill-height" fluid>
        <v-container>
          <v-row dense>
            <v-card>お気に入り</v-card>
            <v-spacer></v-spacer>
            <v-col cols="12">
              <v-card>
                <v-card-title class="headline"
                  >Unlimited music now</v-card-title
                >
                <v-card-subtitle
                  >Listen to your favorite artists and albums whenever and
                  wherever, online and offline.</v-card-subtitle
                >
              </v-card>
            </v-col>
            <v-card>おすすめ</v-card>
            <v-spacer></v-spacer>
            <v-col
              v-for="(recommend, index) in recommendlist"
              :key="index"
              cols="12"
            >
              <v-card>
                <div class="d-flex flex-no-wrap justify-space-between">
                  <v-avatar size="100" tile>
                    <span class="white--text headline">{{
                      recommend.username
                    }}</span>
                  </v-avatar>
                  <div>
                    <v-card-title class="headline" v-if="recommend.status == 0"
                      >Bussy</v-card-title
                    >
                    <v-card-title class="headline" v-if="recommend.status == 1"
                      >Free</v-card-title
                    >
                    <v-card-subtitle>
                      <div>
                        {{ recommend.comment }}
                      </div>
                      <div>
                        {{ recommend.status_update_at }}
                      </div>
                    </v-card-subtitle>
                  </div>
                </div>
              </v-card>
            </v-col>
            <v-card>友達</v-card>
            <v-spacer></v-spacer>
            <v-col
              v-for="friend in friendslist"
              :key="friend.username"
              cols="12"
            >
              <v-card>
                <div class="d-flex flex-no-wrap justify-space-between">
                  <v-avatar size="100" tile>
                    <span class="white--text headline">{{
                      friend.username
                    }}</span>
                  </v-avatar>
                  <div>
                    <v-card-title class="headline" v-if="friend.status == 0"
                      >Bussy</v-card-title
                    >
                    <v-card-title class="headline" v-if="friend.status == 1"
                      >Free</v-card-title
                    >
                    <v-card-subtitle>
                      <div>
                        {{ friend.comment }}
                      </div>
                      <div>{{ friend.status_update_at }}</div>
                    </v-card-subtitle>
                  </div>
                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  layout: "home",
  data: () => ({
    items: [
      {
        name: "jonh",
        static: "EAT",
        comment: "Chinese Food",
        time: "2020-09-08 09:00:00"
      },
      {
        name: "JJJ",
        static: "Movie",
        comment: "Chinese Food",
        time: "2020-09-08 09:00:00"
      }
    ],
    friendslist: [],
    recommendlist: []
  }),
  methods: {
    findData: async function() {
      let userid = this.$store.state.user.userInfo.id;
      const friendslist = await this.$axios.$get(
        "http://127.0.0.1:8000/users/friends",
        {
          params: { id: userid }
        }
      );
      const recommendlist = await this.$axios.$get(
        "http://127.0.0.1:8000/users/recommend",
        {
          params: { id: userid }
        }
      );
      if (friendslist != null) {
        this.friendslist = friendslist;
      }
      if (recommendlist != null) {
        this.recommendlist = recommendlist;
      }
    }
  },
  created() {
    this.findData();
  }
};
</script>

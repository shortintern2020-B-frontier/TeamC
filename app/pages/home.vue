// Author: ZHANG CHI
<template>
  <v-app>
    <v-main>
      <!-- <v-app-bar color="" dense></v-app-bar> -->
      <v-container class="fill-height" fluid>
        <v-container>
          <v-row dense>
            <v-col cols="12">
              <v-card>お気に入り</v-card>
              <v-spacer></v-spacer>
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
            <v-col v-for="(item, index) in items" :key="index" cols="12">
              <v-card>
                <div class="d-flex flex-no-wrap justify-space-between">
                  <v-avatar size="100" tile>
                    <span class="white--text headline">{{ item.name }}</span>
                  </v-avatar>
                  <div>
                    <v-card-title
                      class="headline"
                      v-text="item.static"
                    ></v-card-title>
                    <v-card-subtitle>
                      {{ item.comment }} + {{ item.time }}
                    </v-card-subtitle>
                  </div>
                </div>
              </v-card>
            </v-col>
            <v-card>友達</v-card>
            <v-spacer></v-spacer>
            <v-col v-for="(friend) in friendslist" :key="friend.id" cols="12">
              <v-card>
                <div class="d-flex flex-no-wrap justify-space-between">
                  <v-avatar size="100" tile>
                    <span class="white--text headline">{{
                      friend.username
                    }}</span>
                  </v-avatar>
                  <div>
                    <v-card-title
                      class="headline"
                      v-text="friend.statics"
                    ></v-card-title>
                    <v-card-subtitle>
                      {{ friend.comment }} + {{ friend.status_update_at }}
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
    friendslist: []
  }),
  methods: {
    findData: async function() {
      let userid = this.$store.state.user.userInfo.id;
      const res = await this.$axios.$get(
        "http://127.0.0.1:8000/users/friends",
        {
          params: { id: userid }
        }
      );
      if (res != null) {
        this.friendslist = res;
        console.log(this.friendslist);
      }
    }
  },
  created() {
    this.findData();
  }
};
</script>

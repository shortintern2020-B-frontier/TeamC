// Author: ZHANG CHI
<template>
  <v-app>
    <v-main>
      <!-- <v-app-bar color="" dense></v-app-bar> -->
      <div class="text-center">
        <v-card color="red">
          <v-menu
            bottom
            right
            transition="slide-x-transition"
            origin="top right"
          >
            <template v-slot:activator="{ on }">
              <v-chip-group>
                <v-divider class="mx-1" vertical></v-divider>
                <div v-for="status in statusList" :key="status.id">
                <v-chip label pill v-on="on" @click="search(status.id)">
                  {{status.title}}
                </v-chip>
                </div>
              </v-chip-group>
            </template>
            <v-card width="300">
              <v-list-item v-for="user in searchlist" :key="user.username">
                <v-card>
                  <div class="d-flex flex-no-wrap justify-space-between">
                    <v-avatar size="100" tile>
                      <span class="white--text headline">
                        {{ user.username }}
                      </span>
                    </v-avatar>
                    <div>
                      <v-card-title class="headline" v-if="user.status == 0">
                        Free
                      </v-card-title>
                      <v-card-title class="headline" v-if="user.status == 1">
                        Busy
                      </v-card-title>
                      <v-card-title class="headline" v-if="user.status == 2">
                        Movie
                      </v-card-title>
                      <v-card-title class="headline" v-if="user.status == 3">
                        Karaoke
                      </v-card-title>
                      <v-card-title class="headline" v-if="user.status == 4">
                        Food
                      </v-card-title>
                      <v-card-title class="headline" v-if="user.status == 5">
                        Sports
                      </v-card-title>
                      <v-card-title class="headline" v-if="user.status == 6">
                        Shopping
                      </v-card-title>
                      <v-card-title class="headline" v-if="user.status == 7">
                        Sleeping
                      </v-card-title>
                      <v-card-subtitle>
                        <div>
                          {{ user.comment }}
                        </div>
                        <div>
                          {{ user.status_update_at }}
                        </div>
                      </v-card-subtitle>
                    </div>
                  </div>
                </v-card>
              </v-list-item>
            </v-card>
          </v-menu>
        </v-card>
        <v-divider class="mx-20"></v-divider>
        <v-btn @click="findData">
          Refresh
          <v-icon>mdi-cached</v-icon>
        </v-btn>
      </div>

      <v-container class="fill-height" fluid>
        <v-container>
          <v-row dense>
            <v-card>お気に入り</v-card>
            <v-spacer></v-spacer>
            <v-col cols="12">
              <v-card>
                <div class="d-flex flex-no-wrap justify-space-between">
                  <v-avatar size="100" tile>
                    <span class="white--text headline">
                      Mike
                    </span>
                  </v-avatar>
                  <div>
                    <v-card-title class="headline">
                      Free
                    </v-card-title>
                    <v-card-subtitle>
                      <div>
                        Doing Nothing
                      </div>
                      <div>
                        2020-09-08 09:00:00
                      </div>
                    </v-card-subtitle>
                  </div>
                </div>
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
                    <span class="white--text headline">
                      {{ recommend.username }}
                    </span>
                  </v-avatar>
                  <div>
                    <v-card-title class="headline" v-if="recommend.status == 0">
                      Free
                    </v-card-title>
                    <v-card-title class="headline" v-if="recommend.status == 1">
                      Busy
                    </v-card-title>
                    <v-card-title class="headline" v-if="recommend.status == 2">
                      Movie
                    </v-card-title>
                    <v-card-title class="headline" v-if="recommend.status == 3">
                      Karaoke
                    </v-card-title>
                    <v-card-title class="headline" v-if="recommend.status == 4">
                      Food
                    </v-card-title>
                    <v-card-title class="headline" v-if="recommend.status == 5">
                      Sports
                    </v-card-title>
                    <v-card-title class="headline" v-if="recommend.status == 6">
                      Shopping
                    </v-card-title>
                    <v-card-title class="headline" v-if="recommend.status == 7">
                      Sleeping
                    </v-card-title>
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
            <v-col cols="12"></v-col>
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
                    <span class="white--text headline">
                      {{ friend.username }}
                    </span>
                  </v-avatar>
                  <div>
                    <v-card-title class="headline" v-if="friend.status == 0">
                      Free
                    </v-card-title>
                    <v-card-title class="headline" v-if="friend.status == 1">
                      Busy
                    </v-card-title>
                    <v-card-title class="headline" v-if="friend.status == 2">
                      Movie
                    </v-card-title>
                    <v-card-title class="headline" v-if="friend.status == 3">
                      Karaoke
                    </v-card-title>
                    <v-card-title class="headline" v-if="friend.status == 4">
                      Food
                    </v-card-title>
                    <v-card-title class="headline" v-if="friend.status == 5">
                      Sports
                    </v-card-title>
                    <v-card-title class="headline" v-if="friend.status == 6">
                      Shopping
                    </v-card-title>
                    <v-card-title class="headline" v-if="friend.status == 7">
                      Sleeping
                    </v-card-title>
                    <v-card-subtitle>
                      <div>
                        {{ friend.comment }}
                      </div>
                      <div>
                        {{ friend.status_update_at }}
                      </div>
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
import { mapState } from "vuex";
export default {
  layout: "home",
  data: () => ({
    friendslist: [],
    recommendlist: [],
    searchlist: []
  }),
  methods: {
    findData: async function() {
      let userid = this.$store.state.user.userInfo.id;
      const friendslist = await this.$axios.$get(
        "/users/friends",
        {
          params: { id: userid }
        }
      );
      const recommendlist = await this.$axios.$get(
        "/users/recommend",
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
    },
    search(keyword) {
      this.searchlist = this.friendslist.filter(
        friend => friend.status == keyword
      );
    }
  },
  created() {
    this.findData();
  },
  computed: {
    ...mapState("user", ["statusList"])
  }
};
</script>

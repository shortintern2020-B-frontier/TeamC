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
                    {{ status.title }}
                    <v-icon right>{{ status.class }}</v-icon>
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
                        <v-icon left>
                          mdi mdi-emoticon-happy-outline
                        </v-icon>
                        Free
                      </v-card-title>
                      <v-card-title class="headline" v-if="user.status == 1">
                        <v-icon left>
                          mdi mdi-clock
                        </v-icon>
                        Busy
                      </v-card-title>
                      <v-card-title class="headline" v-if="user.status == 2">
                        <v-icon left>
                          mdi mdi-movie-open
                        </v-icon>
                        Movie
                      </v-card-title>
                      <v-card-title class="headline" v-if="user.status == 3">
                        <v-icon left>
                          mdi mdi-music-note-sixteenth
                        </v-icon>
                        Karaoke
                      </v-card-title>
                      <v-card-title class="headline" v-if="user.status == 4">
                        <v-icon left>
                          mdi mdi-pasta
                        </v-icon>
                        Food
                      </v-card-title>
                      <v-card-title class="headline" v-if="user.status == 5">
                        <v-icon left>
                          mdi mdi-basketball
                        </v-icon>
                        Sports
                      </v-card-title>
                      <v-card-title class="headline" v-if="user.status == 6">
                        <v-icon left>
                          mdi mdi-basket
                        </v-icon>
                        Shopping
                      </v-card-title>
                      <v-card-title class="headline" v-if="user.status == 7">
                        <v-icon left>
                          mdi mdi-power-sleep
                        </v-icon>
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
            <v-col
              v-for="favorite in favoritelist"
              :key="favorite.email"
              cols="12"
            >
              <v-card>
                <div class="d-flex flex-no-wrap justify-space-between">
                  <v-avatar size="100" tile>
                    <span class="white--text headline">
                      {{ favorite.username }}
                    </span>
                  </v-avatar>
                  <div>
                    <v-card-title class="headline" v-if="favorite.status == 0">
                      <v-icon left>
                        mdi mdi-emoticon-happy-outline
                      </v-icon>
                      Free
                    </v-card-title>
                    <v-card-title class="headline" v-if="favorite.status == 1">
                      <v-icon left>
                        mdi mdi-clock
                      </v-icon>
                      Busy
                    </v-card-title>
                    <v-card-title class="headline" v-if="favorite.status == 2">
                      <v-icon left>
                        mdi mdi-movie-open
                      </v-icon>
                      Movie
                    </v-card-title>
                    <v-card-title class="headline" v-if="favorite.status == 3">
                      <v-icon left>
                        mdi mdi-music-note-sixteenth
                      </v-icon>
                      Karaoke
                    </v-card-title>
                    <v-card-title class="headline" v-if="favorite.status == 4">
                      <v-icon left>
                        mdi mdi-pasta
                      </v-icon>
                      Food
                    </v-card-title>
                    <v-card-title class="headline" v-if="favorite.status == 5">
                      <v-icon left>
                        mdi mdi-basketball
                      </v-icon>
                      Sports
                    </v-card-title>
                    <v-card-title class="headline" v-if="favorite.status == 6">
                      <v-icon left>
                        mdi mdi-basket
                      </v-icon>
                      Shopping
                    </v-card-title>
                    <v-card-title class="headline" v-if="favorite.status == 7">
                      <v-icon left>
                        mdi mdi-power-sleep
                      </v-icon>
                      Sleeping
                    </v-card-title>
                    <v-card-subtitle>
                      <div>
                        {{ favorite.comment }}
                      </div>
                      <div>
                        {{ favorite.status_update_at }}
                      </div>
                    </v-card-subtitle>
                  </div>
                </div>
              </v-card>
            </v-col>
            <v-col cols="12"></v-col>
            <v-card>おすすめ</v-card>
            <v-spacer></v-spacer>
            <v-col
              v-for="(recommend, index) in recommendlist"
              :key="index"
              cols="12"
            >
              <!-- <v-card v-if="index == 1"> ss</v-card> -->
              <v-card>
                <div class="d-flex flex-no-wrap justify-space-between">
                  <v-avatar size="100" tile>
                    <span class="white--text headline">
                      {{ recommend.username }}
                    </span>
                  </v-avatar>
                  <div>
                    <v-card-title class="headline" v-if="recommend.status == 0">
                      <v-icon left>
                        mdi mdi-emoticon-happy-outline
                      </v-icon>
                      Free
                    </v-card-title>
                    <v-card-title class="headline" v-if="recommend.status == 1">
                      <v-icon left>
                        mdi mdi-clock
                      </v-icon>
                      Busy
                    </v-card-title>
                    <v-card-title class="headline" v-if="recommend.status == 2">
                      <v-icon left>
                        mdi mdi-movie-open
                      </v-icon>
                      Movie
                    </v-card-title>
                    <v-card-title class="headline" v-if="recommend.status == 3">
                      <v-icon left>
                        mdi mdi-music-note-sixteenth
                      </v-icon>
                      Karaoke
                    </v-card-title>
                    <v-card-title class="headline" v-if="recommend.status == 4">
                      <v-icon left>
                        mdi mdi-pasta
                      </v-icon>
                      Food
                    </v-card-title>
                    <v-card-title class="headline" v-if="recommend.status == 5">
                      <v-icon left>
                        mdi mdi-basketball
                      </v-icon>
                      Sports
                    </v-card-title>
                    <v-card-title class="headline" v-if="recommend.status == 6">
                      <v-icon left>
                        mdi mdi-basket
                      </v-icon>
                      Shopping
                    </v-card-title>
                    <v-card-title class="headline" v-if="recommend.status == 7">
                      <v-icon left>
                        mdi mdi-power-sleep
                      </v-icon>
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
                      <v-icon left>
                        mdi mdi-emoticon-happy-outline
                      </v-icon>
                      Free
                    </v-card-title>
                    <v-card-title class="headline" v-if="friend.status == 1">
                      <v-icon left>
                        mdi mdi-clock
                      </v-icon>
                      Busy
                    </v-card-title>
                    <v-card-title class="headline" v-if="friend.status == 2">
                      <v-icon left>
                        mdi mdi-movie-open
                      </v-icon>
                      Movie
                    </v-card-title>
                    <v-card-title class="headline" v-if="friend.status == 3">
                      <v-icon left>
                        mdi mdi-music-note-sixteenth
                      </v-icon>
                      Karaoke
                    </v-card-title>
                    <v-card-title class="headline" v-if="friend.status == 4">
                      <v-icon left>
                        mdi mdi-pasta
                      </v-icon>
                      Food
                    </v-card-title>
                    <v-card-title class="headline" v-if="friend.status == 5">
                      <v-icon left>
                        mdi mdi-basketball
                      </v-icon>
                      Sports
                    </v-card-title>
                    <v-card-title class="headline" v-if="friend.status == 6">
                      <v-icon left>
                        mdi mdi-basket
                      </v-icon>
                      Shopping
                    </v-card-title>
                    <v-card-title class="headline" v-if="friend.status == 7">
                      <v-icon left>
                        mdi mdi-power-sleep
                      </v-icon>
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
    favoritelist: [],
    friendslist: [],
    recommendlist: [],
    searchlist: []
  }),
  methods: {
    findData: async function() {
      let userid = this.$store.state.user.userInfo.id;
      const favoritelist = await this.$axios.$get("/users/favorites", {
        params: { id: userid }
      });
      const friendslist = await this.$axios.$get("/users/friends", {
        params: { id: userid }
      });
      const recommendlist = await this.$axios.$get("/users/recommend", {
        params: { id: userid }
      });
      if (favoritelist != null) {
        this.favoritelist = favoritelist;
      }
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

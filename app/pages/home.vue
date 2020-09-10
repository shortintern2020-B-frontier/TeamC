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
              <v-list-item
                v-for="user in searchlist"
                :key="`user_${user.username}`"
              >
                <v-card v-bind:to="getIndividualURL(user.user_id)">
                  <div class="d-flex flex-no-wrap justify-space-between">
                    <v-avatar size="70">
                      <img :src="avatar(user.id)" :alt="user.username" />
                    </v-avatar>
                    <span class="headline">
                      {{ user.username }}
                    </span>
                    <div>
                      <v-card-title class="headline">
                        <v-icon left>
                          {{ statusList[user.status].class }}
                        </v-icon>
                        {{ statusList[user.status].title }}
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
        <!-- <v-divider class="mx-20"></v-divider> -->
        <!-- <v-btn @click="findData">
          Recommend Again
          <v-icon>mdi-cached</v-icon>
        </v-btn> -->
      </div>
      <v-container class="fill-height" fluid>
        <v-container>
          <v-row dense>
            <v-card>お気に入り</v-card>
            <v-spacer></v-spacer>
            <v-col
              v-for="favorite in favoritelist"
              :key="`favorite_${favorite.id}`"
              cols="12"
            >
              <v-card v-bind:to="getIndividualURL(favorite.user_id)">
                <div v-if="favorite.id == 0">No favorite</div>
                <div
                  class="d-flex flex-no-wrap justify-space-between"
                  v-if="favorite.id != 0"
                >
                  <v-avatar class="ma-3" size="70" tile>
                    <img :src="avatar(favorite.id)" :alt="favorite.username" />
                  </v-avatar>
                  <span class="headline">
                    {{ favorite.username }}
                  </span>
                  <div>
                    <v-card-title class="headline">
                      <v-icon left>
                        {{ statusList[favorite.status].class }}
                      </v-icon>
                      {{ statusList[favorite.status].title }}
                    </v-card-title>
                    <v-card-subtitle>
                      <div>
                        {{ favorite.comment }}
                      </div>
                      <div>
                        {{ favorite.status_update_at }}
                      </div>
                      <div class="distance">
                        {{ getDistance(favorite) }}
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
              <v-card v-if="index == 0" class="text-center">
                <div class="text-center">
                  <v-avatar class="ma-3" size="70">
                    <img :src="avatar(userInfo.id)" :alt="userInfo.username" />
                  </v-avatar>
                  <v-avatar class="ma-3" size="70">
                    <img
                      :src="avatar(recommend.id)"
                      :alt="recommend.username"
                    />
                  </v-avatar>
                </div>
                <v-card-text class="headline text-center">
                  一緒に{{ statusList[recommend.status].title }}しない？
                </v-card-text>
                <v-btn
                  class="ma-3"
                  v-if="invited == false"
                  @click="sendInvites(recommend.id)"
                >
                  ok
                </v-btn>
                <v-progress-circular
                  indeterminate
                  color="primary"
                  class="ma-3"
                  v-if="invited == true"
                  >Waiting for confirmation
                </v-progress-circular>
              </v-card>
              <v-card>
                <div
                  class="d-flex flex-no-wrap justify-space-between"
                  v-if="index != 0"
                >
                  <v-avatar class="ma-3" size="70" tile>
                    <img
                      :src="avatar(recommend.id)"
                      :alt="`recommend_${recommend.username}`"
                    />
                  </v-avatar>
                  <span class="headline">
                    {{ recommend.username }}
                  </span>
                  <div>
                    <v-card-title class="headline">
                      <v-icon left>
                        {{ statusList[recommend.status].class }}
                      </v-icon>
                      {{ statusList[recommend.status].title }}
                    </v-card-title>
                    <v-card-subtitle>
                      <div>
                        {{ recommend.comment }}
                      </div>
                      <div>
                        {{ recommend.status_update_at }}
                      </div>
                      <div class="distance">
                        {{ getDistance(recommend) }}
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
              :key="`friend_${friend.username}`"
              cols="12"
            >
              <v-card v-bind:to="getIndividualURL(friend.user_id)">
                <div v-if="friend.id == 0">No Friends</div>
                <div
                  class="d-flex flex-no-wrap justify-space-between"
                  v-if="friend.id != 0"
                >
                  <v-avatar class="ma-3" size="70" tile>
                    <img :src="avatar(friend.id)" :alt="friend.username" />
                  </v-avatar>
                  <span class="headline">
                    {{ friend.username }}
                  </span>
                  <div>
                    <v-card-title class="headline">
                      <v-icon left>
                        {{ statusList[friend.status].class }}
                      </v-icon>
                      {{ statusList[friend.status].title }}
                    </v-card-title>
                    <v-card-subtitle>
                      <div>
                        {{ friend.comment }}
                      </div>
                      <div>
                        {{ friend.status_update_at }}
                      </div>
                      <div class="distance">
                        {{ getDistance(friend) }}
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
import calcDistance from "@/modules/calcDistance";
export default {
  layout: "home",
  data: () => ({
    favoritelist: [{ id: 0 }],
    friendslist: [{ id: 0 }],
    recommendlist: [],
    searchlist: [],
    invited: false,
    invitedlist: []
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
      const invitedStatus = await this.$axios.$post("/invites/recommend", {
        host_user_id: userid,
        guest_user_id: recommendlist[0].id
      });
      if (favoritelist.length != 0) {
        this.favoritelist = favoritelist;
      }
      if (friendslist.length != 0) {
        this.friendslist = friendslist;
      }
      if (recommendlist.length != 0) {
        this.recommendlist = recommendlist;
      }
      if (invitedStatus[0].valid_status == 2) {
        this.invited = true;
      }
    },
    search(keyword) {
      this.searchlist = this.friendslist.filter(
        friend => friend.status == keyword
      );
    },
    getDistance(friend) {
      if (
        this.$store.state.user.userInfo.latitude != null &&
        friend.latitude != null
      ) {
        let dis = calcDistance(
          this.$store.state.user.userInfo.latitude,
          this.$store.state.user.userInfo.longitude,
          friend.latitude,
          friend.longitude
        );

        return dis.toFixed(1).toString() + " km";
      } else {
        return "";
      }
    },
    getIndividualURL(id){
      return "/individual_user_info?user_id=" + id
    },
    sendInvites: function(guest_user_id) {
      let _this = this;
      this.$axios({
        method: "post",
        url: "/invites/create",
        data: {
          host_user_id: this.$store.state.user.userInfo.id,
          guest_user_id: guest_user_id
        }
      })
        .then(function(response) {
          if (response.data == null) {
          } else {
            _this.invited = true;
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  },
  created() {
    this.findData();
  },
  computed: {
    ...mapState("user", ["statusList", "userInfo"]),
    avatar() {
      return id => {
        const imageLen = 10;
        return `/user_icon_${(id % imageLen) + 1}.jpg`;
      };
    }
  }
};
</script>

<!-- Author:ZHANG CHI-->
<template>
  <v-app>
    <v-main>
      <!-- <v-app-bar color="" dense></v-app-bar> -->
      <div class="text-center">
        <v-card color="deep-purple lighten-1" tile>
          <v-menu
            bottom
            right
            transition="slide-x-transition"
            origin="top right"
          >
            <template v-slot:activator="{ on }">
              <v-chip-group>
                <div class="mx-1" vertical></div>
                <div v-for="status in statusList" :key="status.id">
                  <v-chip
                    color="deep-purple lighten-5"
                    label
                    pill
                    v-on="on"
                    @click="search(status.id)"
                  >
                    {{ status.title }}
                    <v-icon right>{{ status.class }}</v-icon>
                  </v-chip>
                </div>
              </v-chip-group>
            </template>
            <v-card flat width="100%">
              <v-list-item
                v-for="user in searchlist"
                :key="`user_${user.username}`"
              >
                <v-card
                  class="ma-3"
                  flat
                  v-bind:to="getIndividualURL(user.user_id)"
                >
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
            <v-card>Favorite</v-card>
            <v-spacer></v-spacer>
            <v-col
              v-for="favorite in favoritelist"
              :key="`favorite_${favorite.id}`"
              cols="12"
            >
            <div v-if="favorite.id == 0">No favorite</div>
              <v-card v-bind:to="getIndividualURL(favorite.user_id)">
                
                <div
                  class="d-flex flex-no-wrap justify-space-between"
                  v-if="favorite.id != 0"
                >
                  <v-avatar class="ma-3" size="70">
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
            <v-card>Recommend</v-card>
            <v-spacer></v-spacer>
            <v-col
              v-for="(recommend, index) in recommendlist"
              :key="index"
              cols="12"
            >
              <div v-if="recommend.id == 0">No Recommend</div>
              <v-card
                v-if="index == 0 && recommend.id != 0"
                class="text-center"
              >
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
                  Let's {{ statusList[recommend.status].title }} !
                </v-card-text>
                <v-btn
                  class="ma-3"
                  v-if="invited == false"
                  @click="sendInvites(recommend.id)"
                >
                  Invite
                </v-btn>
                <v-container v-if="invited == true && invitedconfirm == false"
                  ><v-progress-circular
                    indeterminate
                    color="deep-purple accent-3"
                    class="ma-3"
                  >
                  </v-progress-circular
                  >Waiting for confirmation</v-container
                >

                <v-btn
                  class="ma-3"
                  v-if="invited == true && invitedconfirm == true"
                  disabled
                >
                  invited
                </v-btn>
              </v-card>
              <v-card v-bind:to="getIndividualURL(recommend.user_id)">
                <div
                  class="d-flex flex-no-wrap justify-space-between"
                  v-if="index != 0"
                >
                  <v-avatar class="ma-3" size="70">
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
            <v-card>friends</v-card>
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
                  <v-avatar class="ma-3" size="70">
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
    recommendlist: [{ id: 0 }],
    searchlist: [],
    invited: false,
    invitedconfirm: false,
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
      let invitedStatus = [];
      if (recommendlist.length > 0) {
        invitedStatus = await this.$axios.$post("/invites/confirm", {
          host_user_id: userid,
          guest_user_id: recommendlist[0].id
        });
      }
      if (favoritelist.length != 0) {
        this.favoritelist = favoritelist;
      }
      if (friendslist.length != 0) {
        this.friendslist = friendslist;
      }
      if (recommendlist.length != 0 && this.$store.state.user.userInfo.status !=1) {
        this.recommendlist = recommendlist;
      }
      if (invitedStatus.length > 0 && invitedStatus[0].valid_status == 2) {
        this.invited = true;
      }
      if (invitedStatus.length > 0 && invitedStatus[0].valid_status == 1) {
        this.invited = true;
        this.invitedconfirm = true;
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
    getIndividualURL(id) {
      return "/individual_user_info?user_id=" + id;
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
  async created() {
    await this.findData();
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
